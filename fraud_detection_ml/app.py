from src.predict import predict_fraud
import streamlit as st
import pandas as pd
import joblib

from sklearn.preprocessing import StandardScaler
st.title("💳 Fraud Detection")

time = st.number_input("Time")
amount = st.number_input("Amount")
#X_test = joblib.load('data/X_test.pkl')
X_test = pd.read_csv("data/X_test.csv")

features =X_test.iloc[0].copy()

features.iloc[-1]=amount
features.iloc[0]=time
features = features.tolist()
#features = [time] + [0]*28 + [amount]

if st.button("Predict"):
    result = predict_fraud(features)

    if result == "Fraud":
        st.error("🚨 Fraud Detected!")
    else:
        st.success("✅ Normal Transaction")