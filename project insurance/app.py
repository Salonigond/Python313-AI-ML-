import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Insurance Charges Predictor", layout="wide")

# Load Models
@st.cache_resource
def load_models():
    rf_model = joblib.load('rf_model.pkl')
    preprocessor = joblib.load('preprocessor.pkl')
    return rf_model, preprocessor

rf_model, preprocessor = load_models()

# Title
st.title("💰 Insurance Charges Prediction App")
st.markdown("Predict medical insurance charges using Linear Regression & Random Forest")

# Sidebar - User Input
st.sidebar.header("Enter Patient Details")

def user_input():
    age = st.sidebar.slider("Age", 18, 100, 30)
    sex = st.sidebar.selectbox("Sex", ["male", "female"])
    bmi = st.sidebar.slider("BMI", 15.0, 50.0, 25.0, 0.1)
    children = st.sidebar.selectbox("Children", [0, 1, 2, 3, 4, 5])
    smoker = st.sidebar.selectbox("Smoker", ["yes", "no"])
    region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

    data = {
        'age': age,
        'sex': sex,
        'bmi': bmi,
        'children': children,
        'smoker': smoker,
        'region': region
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input()

# Main Panel
col1, col2 = st.columns(2)

with col1:
    st.subheader("Patient Details")
    st.write(input_df)

with col2:
    st.subheader("Prediction")

    if st.button("Predict Charges", type="primary"):
        # Preprocess Input
        input_encoded = preprocessor.transform(input_df)

        # Predict
        prediction = rf_model.predict(input_encoded)

        st.success(f"💵 Predicted Insurance Charges: ${prediction[0]:,.2f}")

        # Feature Importance
        st.subheader("What Affects Charges Most?")
        importances = rf_model.feature_importances_
        feature_names = preprocessor.get_feature_names_out()

        feat_imp = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values('Importance', ascending=False).head(5)

        st.bar_chart(feat_imp.set_index('Feature'))

# Footer Info
st.markdown("---")
st.markdown("**Model**: Random Forest Regressor | **R² Score**: ~0.86 | **RMSE**: ~$4600")