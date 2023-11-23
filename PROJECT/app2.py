import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes = pickle.load(open("diabetes.pkl", "rb"))

selected = option_menu("Multiple Disease Prediction System using Machine Learning", 
                           
                           ["Diabetes Prediction"
                            ],   
                           default_index = 0)

if(selected == "Diabetes Prediction"):
    
    #page title
    st.title("Diabetes Prediction using Machine Learning")
    
    

# getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=22, max_value=93, value=44)
        
    with col2:
        bmi = st.number_input("BMI (kg/m2)", min_value=15.6, max_value=50.0, value=25.7)
    
    with col3:
        fpg = st.number_input("FPG", min_value=1.78, max_value=10.0, value=6.69,help="FPG (Fasting Plasma Glucose)")
    
    with col1:
        ffpg = st.number_input("FFPG", min_value=3.2, max_value=35.0, value=7.4,help="FFPG (Final Fasting Plasma Glucose)")
    
    with col2:
        sbp = st.number_input("SBP (mmHg)", min_value=72.0, max_value=218.0, value=105.0,help="SBP (Systolic Blood Pressure)")
    
    with col3:
        dbp = st.number_input("DBP",min_value=45,max_value=140,value=78,help="DBP (Diastolic Blood Pressure)")
    
    with col1:
        family_history = st.number_input("Family History", min_value=0, max_value=1, value=0)
    
    with col2:
        smoking = st.number_input("Smoking", min_value=1, max_value=3, value=3,help="Smoking Status: 1: Current Smoker, 2: Ever Smoker, 3: Never Smoker")

    with col3:
        drinking = st.number_input("Drinking", min_value=1, max_value=3, value=3,help="Drinking Status: 1: Current Drinker, 2: Ever Drinker, 3: Never Drinker")
    
    with col1:
        alt = st.number_input("ALT", min_value=4.5, max_value=440.0, value=48.0)


# code for Prediction
    diabetes_diagnosis = " "
    
    # creating a button for Prediction
    
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes.predict([[age, bmi, fpg, ffpg, sbp,dbp, family_history, smoking, drinking, alt]])
        
        if (diabetes_prediction[0] == 0):
          diabetes_diagnosis = "Hurrah! You have no Diabetes."
        else:
          diabetes_diagnosis = "Sorry! You have Diabetes."
        
    st.success(diabetes_diagnosis)