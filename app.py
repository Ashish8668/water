from flask import Flask, render_template, request
import pickle

import pandas as pd

app = Flask(__name__)

# Load model and scaler
with open('svc_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Maintain same order as used during training
        columns = [
            'ph', 'Hardness', 'Solids', 'Chloramines', 
            'Sulfate', 'Conductivity', 'Organic_carbon', 
            'Trihalomethanes', 'Turbidity'
        ]

        # Collect inputs in correct order and convert to float
        features = [float(request.form[col]) for col in columns]

        # Create a DataFrame to avoid feature name warnings
        input_df = pd.DataFrame([features], columns=columns)

        # Scale input
        scaled_features = scaler.transform(input_df)

        # Predict potability
        prediction = model.predict(scaled_features)[0]

        # Convert numeric output to readable form
        result = "Safe for Drinking" if prediction == 1 else "Not Safe for Drinking"

        return render_template('result.html', prediction=result)

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True,port=5000)
