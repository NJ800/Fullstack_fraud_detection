from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import joblib
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory="templates")

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_columns = joblib.load("feature_columns.pkl")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "features": feature_columns,
            "prediction": None
        }
    )


@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):

    form_data = await request.form()

    input_data = {
        key: float(value)
        for key, value in form_data.items()
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df[feature_columns]

    input_scaled = scaler.transform(input_df)

    probability = model.predict_proba(input_scaled)[0][1]

    is_fraud = probability > 0.5

    # Risk Level Classification
    if probability < 0.3:
        risk_level = "Low Risk"
        bar_color = "bg-success"
    elif probability < 0.7:
        risk_level = "Medium Risk"
        bar_color = "bg-warning"
    else:
        risk_level = "High Risk"
        bar_color = "bg-danger"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "features": feature_columns,
            "prediction": {
                "probability": round(float(probability), 4),
                "is_fraud": is_fraud,
                "risk_level": risk_level,
                "bar_color": bar_color
            }
        }
    )