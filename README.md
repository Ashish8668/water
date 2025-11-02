# 💧 Neeralyze — Water Potability Prediction

Neeralyze is a **Flask-based web application** that predicts the **potability of water** using **Machine Learning**.  
The system analyzes various **physicochemical parameters** of water to determine whether it is **safe for drinking** or not.

🌐 **Live Demo:** [https://neeralyze.onrender.com/](https://neeralyze.onrender.com/)

---

## 📋 Problem Statement

Access to safe drinking water is a fundamental human need. However, water contamination remains a major global issue.  
Manual testing methods are often slow and unreliable.  
This project aims to build an **intelligent system** that can predict water potability using **machine learning** techniques, improving accuracy and speed of analysis.

---

## 🎯 Project Objectives

1. Develop a **Support Vector Classifier (SVC)** model to predict water potability.
2. Build a **Flask web app** for user input and instant potability prediction.
3. Apply **data preprocessing** and **feature scaling** for better model accuracy.
4. Visualize and analyze dataset characteristics for validation.
5. Deploy the app securely using **Gunicorn** and **Render Cloud**.

---

## 🧠 Methodology

### Steps Followed

1. **Data Collection**
   - Features: `pH`, `Hardness`, `Solids`, `Chloramines`, `Sulfate`, `Conductivity`, `Organic Carbon`, `Trihalomethanes`, `Turbidity`, `Potability`.

2. **Data Preprocessing**
   - Missing values handled using `KNNImputer`.
   - Feature scaling via `StandardScaler`.
   - Split data into **80% training** and **20% testing**.
   - Dataset distribution: 60% Non-potable, 40% Potable.

3. **Model Building**
   - Trained **Support Vector Classifier (SVC)** using `scikit-learn`.
   - Saved trained model and scaler using `pickle`.

4. **Web Application**
   - Flask app with `index.html` for input form and `result.html` for displaying output.
   - Integrated the trained model for **real-time prediction**.

5. **Deployment**
   - Hosted on [Render](https://render.com/) using **Gunicorn** for production-grade performance and security.

---

## 🧰 Technology Stack

| Category | Tools / Technologies |
|-----------|----------------------|
| **Language** | Python 3.11 |
| **Libraries** | pandas, numpy, scikit-learn, pickle |
| **Framework** | Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **ML Model** | Support Vector Classifier (SVC) |
| **Deployment** | Gunicorn + Render |

---

## ⚙️ Local Setup Instructions

Follow these steps to **clone** and **run** the Flask app locally:

### 1️⃣ Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows
```

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Ashish8668/water.git
cd water
```

### 3️⃣ Install Dependencies Run Neeralyze
```bash
pip install -r requirements.txt
python app.py
```

