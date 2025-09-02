import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/health_model.pkl")

st.title("🚑 AI-Enabled Health Monitoring System")

# Input fields
heart_rate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, value=72)
blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=80, max_value=200, value=120)
temperature = st.number_input("Temperature (°F)", min_value=95.0, max_value=105.0, value=98.6)

if st.button("Check Condition"):
    features = np.array([[heart_rate, blood_pressure, temperature]])
    prediction = model.predict(features)[0]

    if prediction == 0:
        st.success("✅ Patient is Healthy")
    else:
        st.error("⚠️ Patient may be at Risk! Consult a Doctor.")
