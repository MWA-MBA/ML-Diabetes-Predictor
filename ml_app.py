
import streamlit as st
import pandas as pd
import joblib
import os

# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the trained ML model and scaler
try:
    best_ml_model = joblib.load(os.path.join(BASE_DIR, 'best_xgb_weighted_model.joblib'))
    scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.joblib'))
except FileNotFoundError as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

st.set_page_config(layout="wide")
st.title('Diabetes Prediction (Machine Learning Model)')

st.write("### Enter Patient Information:")

# Define input fields for the 8 features
with st.form("prediction_form"):
    pregnancies = st.slider('Pregnancies', 0, 17, 3)
    glucose = st.slider('Glucose', 44, 199, 117) # Median from pre-imputation was 117
    blood_pressure = st.slider('Blood Pressure', 24, 122, 72) # Median from pre-imputation was 72
    skin_thickness = st.slider('Skin Thickness', 7, 99, 29) # Median from pre-imputation was 29
    insulin = st.slider('Insulin', 14, 846, 125) # Median from pre-imputation was 30.5, but scaled later, adjusted to 125 for range.
    bmi = st.slider('BMI', 18.2, 67.1, 32.3) # Median from pre-imputation was 32.3
    diabetes_pedigree_function = st.slider('Diabetes Pedigree Function', 0.078, 2.42, 0.3725)
    age = st.slider('Age', 21, 81, 29)

    submitted = st.form_submit_button("Predict")

    if submitted:
        # Create a DataFrame from the inputs
        input_data = pd.DataFrame([{
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'BloodPressure': blood_pressure,
            'SkinThickness': skin_thickness,
            'Insulin': insulin,
            'BMI': bmi,
            'DiabetesPedigreeFunction': diabetes_pedigree_function,
            'Age': age
        }])

        # Scale the input data using the loaded scaler
        scaled_input_data = scaler.transform(input_data)

        # Make prediction
        prediction = best_ml_model.predict(scaled_input_data)
        prediction_proba = best_ml_model.predict_proba(scaled_input_data)[:, 1]

        st.write("### Prediction Result:")
        if prediction[0] == 1:
            st.error(f"The model predicts diabetes with a probability of {prediction_proba[0]:.2f}")
        else:
            st.success(f"The model predicts no diabetes with a probability of {1 - prediction_proba[0]:.2f}")
