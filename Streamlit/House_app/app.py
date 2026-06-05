# app.py

import streamlit as st
import numpy as np
import joblib
from scaler import load_scaler, transform_data

# Load model & scaler
model = joblib.load("model.pkl")
scaler = load_scaler()

st.title("House Price Prediction")

area = st.number_input("Area", 500, 10000, 1000)
bedrooms = st.number_input("Bedrooms", 1, 10, 2)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)

if st.button("Predict"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    input_scaled = transform_data(scaler, input_data)

    prediction = model.predict(input_scaled)
    st.success(f"Price: ₹ {int(prediction[0]):,}")