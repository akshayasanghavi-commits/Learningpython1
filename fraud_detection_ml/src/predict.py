import numpy as np

import pickle

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model/fraud_model.pkl", "rb") as f:
    model = pickle.load(f)
threshold = 0.4
def predict_fraud(input_data):
    input_array = np.array(input_data).reshape(1, -1)#“Reshaping converts input data into the required 2D format so that the model can process it correctly, even for a single sample
    input_scaled = scaler.transform(input_array)

   # prediction = model.predict(input_scaled)

   # return "Fraud" if prediction[0] == 1 else "Not Fraud"
    prob = model.predict_proba(input_scaled)[0][1]

    return "Fraud" if prob > threshold else "Not Fraud"