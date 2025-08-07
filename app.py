# app.py
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("app_cost_model.pkl")

st.title("📱 Custom App Cost Estimator")

# Inputs
platform = st.selectbox("Select Platform", ["Android", "iOS", "Both"])
complexity = st.selectbox("App Complexity", ["Simple", "Medium", "Complex"])
auth = st.checkbox("User Authentication?")
backend = st.checkbox("Backend Required?")
payment = st.checkbox("Payment Integration?")
realtime = st.checkbox("Real-time Features?")
screens = st.slider("Number of Screens", 1, 50, 10)
duration = st.slider("Estimated Duration (weeks)", 1, 24, 12)

# Prepare input
input_data = pd.DataFrame([{
    'platform': platform,
    'complexity': complexity,
    'auth': int(auth),
    'backend': int(backend),
    'payment': int(payment),
    'realtime': int(realtime),
    'screens': screens,
    'duration': duration
}])

# Predict cost
if st.button("Estimate Cost 💰"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Development Cost: **${int(prediction):,}**")
