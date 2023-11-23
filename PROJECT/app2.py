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
        age = st.text_input("Age")
        
    with col2:
        bmi = st.text_input("BMI")
    
    with col3:
        fpg = st.text_input("FPG")
    
    with col1:
        ffpg = st.text_input("FFPG")
    
    with col2:
        sbp = st.text_input("SBP")
    
    with col3:
        dbp = st.text_input("DBP")
    
    with col1:
        family_history = st.text_input("Family History")
    
    with col2:
        smoking = st.text_input("Smoking")

    with col3:
        drinking = st.text_input("drinking")
    
    with col1:
        alt = st.text_input("ALT")


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