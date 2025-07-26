import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

# Load trained model (We’ll create this below)
model = pickle.load(open('heart_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Streamlit UI
st.title("🫀 Heart Disease Prediction App")
st.write("Enter your health information below:")

# Input fields
age = st.number_input('Age', min_value=1, max_value=120, value=30)
sex = st.selectbox('Sex', ['Male', 'Female'])
cp = st.selectbox('Chest Pain Type (cp)', [0,1,2,3])
trestbps = st.number_input('Resting Blood Pressure', value=120)
chol = st.number_input('Cholesterol', value=200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)', [0,1])
restecg = st.selectbox('Resting ECG Results', [0,1,2])
thalach = st.number_input('Maximum Heart Rate Achieved', value=150)
exang = st.selectbox('Exercise Induced Angina (1 = Yes, 0 = No)', [0,1])
oldpeak = st.number_input('ST depression induced by exercise', value=1.0)
slope = st.selectbox('Slope of peak exercise ST segment', [0,1,2])
ca = st.selectbox('Number of major vessels (0-3)', [0,1,2,3])
thal = st.selectbox('Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)', [1,2,3])

# Prepare input data
input_data = np.array([[age, 1 if sex=='Male' else 0, cp, trestbps, chol, fbs,
                        restecg, thalach, exang, oldpeak, slope, ca, thal]])

# Scale input
input_data_scaled = scaler.transform(input_data)

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_data_scaled)
    probability = model.predict_proba(input_data_scaled)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠️ High Risk of Heart Disease (Probability: {probability*100:.2f}%)")
    else:
        st.success(f"✅ Low Risk of Heart Disease (Probability: {probability*100:.2f}%)")
