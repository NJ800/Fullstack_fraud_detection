# 💳 Fraud Detection System – Full Stack ML Web Application

## 📌 Project Overview

This project is an end-to-end Machine Learning web application that
detects fraudulent financial transactions in real time.  
It integrates a trained classification model with a Flask backend and a
responsive frontend interface.

The system demonstrates the complete ML lifecycle from data
preprocessing and model training to deployment and real-time prediction.

------------------------------------------------------------------------

## 🏗️ Tech Stack

### 🔹 Frontend

-   HTML5  
-   CSS3  
-   JavaScript

### 🔹 Backend

-   Python  
-   Flask

### 🔹 Machine Learning

-   Scikit-learn  
-   Pandas  
-   NumPy  
-   Joblib

------------------------------------------------------------------------

## 📂 Project Structure

    fraud_detection_fullstack/
    │
    ├── static/
    │   ├── style.css
    │   └── script.js
    │
    ├── templates/
    │   └── index.html
    │
    ├── model/
    │   ├── fraud_model.pkl
    │   └── scaler.pkl
    │
    ├── app.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## 🧠 Machine Learning Workflow

1.  Data Cleaning and Preprocessing  
2.  Feature Engineering  
3.  Feature Scaling using StandardScaler  
4.  Model Training (Classification Model)  
5.  Model Evaluation  
6.  Model Saving using Joblib  
7.  Integration with Flask Backend

------------------------------------------------------------------------

## ⚙️ How the System Works

1.  User enters transaction details in the web interface.  
2.  Data is sent to the Flask backend via POST request.  
3.  Backend loads the trained model and scaler.  
4.  Input features are scaled.  
5.  Model predicts fraud probability.  
6.  If probability exceeds threshold → **Fraud**  
7.  Otherwise → **Legitimate Transaction**

------------------------------------------------------------------------

## 📡 API Endpoint

### POST `/predict`

### Example Request

``` json
{
  "feature1": 1.25,
  "feature2": 4500,
  "feature3": 0.67
}
```

### Example Response

``` json
{
  "prediction": "Fraud",
  "probability": 0.84
}
```

------------------------------------------------------------------------

## 🚀 Installation Guide

### 1️⃣ Clone the Repository

    git clone https://github.com/your-username/fraud-detection.git
    cd fraud-detection

### 2️⃣ Create Virtual Environment

    python -m venv venv

Activate:

**Windows**

    venv\Scripts\activate

**Mac/Linux**

    source venv/bin/activate

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Run Application

    python app.py

Open in browser:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📊 Key Features

-   Real-time fraud probability prediction  
-   Scaler and model integration  
-   Threshold-based classification logic  
-   Clean full-stack architecture  
-   REST API communication  
-   Modular project structure

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Add transaction history database  
-   Implement user authentication  
-   Deploy to AWS / Render  
-   Add analytics dashboard  
-   Improve model performance with ensemble methods

------------------------------------------------------------------------

## 👨‍💻 Author

**Nikhil Jain**  
Full Stack & Machine Learning Developer
