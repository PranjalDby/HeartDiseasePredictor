import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
def cap_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return series.apply(lambda x: upper if x > upper else lower if x < lower else x)

######## ----------------------------------------------------- main Logic
if os.path.exists('./model_res'):
    st.write('Running model...')


## loading the model
with open('model_res/decision_treeModel.pkl', 'rb') as f:
    model = pickle.load(f)

# You may need to load scaler, imputer, and pca as well
with open('./model_res/scaler_.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('./model_res/imputer_.pkl', 'rb') as f:
    imputer = pickle.load(f)

with open('./model_res/pca.pkl', 'rb') as f:
    pca = pickle.load(f)


st.title('Heart Disease Prediction')

# Example input fields (customize as needed)
age = st.number_input('Age', min_value=0, max_value=120, value=50)
trestbps = st.number_input('Resting Blood Pressure', min_value=80, max_value=200, value=120)
chol = st.number_input('Cholesterol', min_value=100, max_value=600, value=200)
fbs = st.number_input('Fasting Blood Sugar', min_value=0, max_value=1, value=0)
exang = st.number_input('Exercise Induced Angina', min_value=0, max_value=1, value=0)

# Additional columns
sex = st.number_input('Sex (1 = male, 0 = female)', min_value=0, max_value=1, value=1)
cp = st.number_input('Chest Pain Type (0-3)', min_value=0, max_value=3, value=0)
thalach = st.number_input('Maximum Heart Rate Achieved', min_value=60, max_value=220, value=150)
slope = st.number_input('Slope of Peak Exercise ST Segment (0-2)', min_value=0, max_value=2, value=1)
ca = st.number_input('Number of Major Vessels (0-3)', min_value=0, max_value=3, value=0)
thal = st.number_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)', min_value=1, max_value=3, value=2)
restecg = st.number_input('Resting Electrocardiographic Results (0-2)', min_value=0, max_value=2, value=1)

__cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']
if st.button('Predict'):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
       exang, 0, slope, ca, thal]])
    # Note: Replace 'oldpeak' and 'target' (currently set to 0) with actual input values if needed.
    
    input_data = pd.DataFrame(input_data,columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    #preprocessing the input
    input_data = scaler.transform(input_data)
    input_data = imputer.transform(input_data)
    input_data = pca.transform(input_data)

    prediction = model.predict(input_data)

    st.write('Prediction:','Heart Disease' if prediction[0] == 1 else 'No Heart Disease')
