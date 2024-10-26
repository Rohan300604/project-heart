import streamlit as st
import pickle
import numpy as np

# Load the logistic regression model
with open('logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Display an image at the top
st.image("R.jpeg", caption="Heart Health Prediction", use_column_width=True)

st.title("Heart Disease Prediction App")
st.write("Fill in the following information to check your heart disease risk.")

# Gender
male = st.selectbox("Gender", ["Male", "Female"])
male = 1 if male == "Male" else 0

# Other input fields for user information
age = st.number_input("Age", min_value=1, max_value=120, step=1)
currentSmoker = st.selectbox("Are you a current smoker?", ["Yes", "No"])
currentSmoker = 1 if currentSmoker == "Yes" else 0

cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, step=1)
BPMeds = st.selectbox("Are you on Blood Pressure Meds?", ["Yes", "No"])
BPMeds = 1 if BPMeds == "Yes" else 0

prevalentStroke = st.selectbox("History of Stroke?", ["Yes", "No"])
prevalentStroke = 1 if prevalentStroke == "Yes" else 0

prevalentHyp = st.selectbox("Do you have Hypertension?", ["Yes", "No"])
prevalentHyp = 1 if prevalentHyp == "Yes" else 0

diabetes = st.selectbox("Do you have Diabetes?", ["Yes", "No"])
diabetes = 1 if diabetes == "Yes" else 0

totChol = st.number_input("Total Cholesterol", min_value=0.0)
sysBP = st.number_input("Systolic Blood Pressure", min_value=0.0)
diaBP = st.number_input("Diastolic Blood Pressure", min_value=0.0)
BMI = st.number_input("Body Mass Index (BMI)", min_value=0.0)
heartRate = st.number_input("Heart Rate", min_value=0, step=1)
glucose = st.number_input("Glucose Level", min_value=0.0)

# Button to predict
if st.button("Predict Heart Disease Risk"):
    # Prepare the feature array
    features = np.array([[male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, 
                          prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose]])

    # Predict using the loaded model
    try:
        prediction = model.predict(features)[0]
        if prediction == 1:
            st.success("The model predicts a high likelihood of heart disease.")
        else:
            st.success("The model predicts a low likelihood of heart disease.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
