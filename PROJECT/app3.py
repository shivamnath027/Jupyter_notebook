import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the gestation model
# pickle_in_gestation = open("knn.pkl", "rb")
# knn_gest = pickle.load(pickle_in_gestation)

# Load the heart disease model
pickle_in_heart = open("diabetes.pkl", "rb")
rf_diab = pickle.load(pickle_in_heart)

# Set page configurations
st.set_page_config(
    page_title="Arogya Vicharana",
    page_icon=":clipboard:",
    layout="wide",
)

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox(
        "AROGYA VICHARANA",
        ['Diabetes Prediction', 'Gestation Diabetes Prediction', 'Diabetes Heart Prediction'],
    )

# Page title
st.title("Arogya Vicharana")

if selected == "Gestation Diabetes Prediction":
    # Page title
    st.header("Gestational Diabetes Prediction")


def predict_note_authentication(age, bmi, fpg, ffpg, sbp,dbp, smoking, drinking, alt):
    
    """Let's predict the disease 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name:age
        in: query
        type: number
        required: true
      - name:bmi
        in: query
        type: number
        required: true
      - name:fpg
        in: query
        type: number
        required: true
      - name:ffpg
        in: query
        type: number
        required: true
      - name:sbp
        in: query
        type: number
        required: true
      - name:dbp
        in: query
        type: number
        required: true
      - name:dbp
        in: query
        type: number
        required: true
      - name:smoking
        in: query
        type: number
        required: true
     - name:drinking
        in: query
        type: number
        required: true
     - name:alt
        in: query
        type: number
        required: true
     
    responses:
        200:
            description: The output values
        
    """
    try:
      # Convert input values to appropriate types
      # Assuming you have these parameters as strings
      age = int(age)
      bmi = float(bmi)
      fpg = float(fpg)
      ffpg = float(ffpg)
      sbp = float(sbp)
      dbp = int(dbp)
      family_history = int(family_history)
      smoking = int(smoking)
      drinking = int(drinking)
      alt = float(alt)
      Dia_BP = float(Dia_BP)
      OGTT = int(OGTT)
      Hemoglobin = float(Hemoglobin)
      Sedentary_Lifestyle = int(Sedentary_Lifestyle)
      Prediabetes = int(Prediabetes)


      # Use numpy array for prediction
      input_values = [age,bmi,fpg,ffpg,sbp,dbp,family_history,smoking,drinking,alt]
      # Use numpy array for prediction
      prediction = rf_diab.predict([input_values]) 
      print(prediction)
      return prediction
    except ValueError as e:
        print(f"Error: {e}")
        return "Invalid input. Please provide valid numeric values for all input fields."


def main():
    st.title("")
    html_temp = """
    # <div style="background-color:;padding:10px">
    # <h2 style="color:white;text-align:center;"></h2>
    # </div>
    # """
    st.markdown(html_temp,unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# col1
with col1:
    age = st.number_input("age", min_value=0, max_value=100, placeholder="Enter age")
    bmi = st.number_input("bmi", min_value=0, max_value=10, key="bmi", placeholder="Type Here")
    fpg = st.number_input("fpg", min_value=0, max_value=100, key="fpg", placeholder="Type Here")
    ffpg = st.number_input("ffpg", min_value=10.0, max_value=40.0, key="ffpg", placeholder="Type Here")
    sbp = st.number_input("sbp", min_value=20, max_value=100, key="sbp", placeholder="Type Here")

# col2
with col2:    
    dbp = st.number_input("dbp", min_value=0, max_value=1, key="dbp", placeholder="Type Here")
    family_history = st.number_input("family_history", min_value=0, max_value=10, key="family_history", placeholder="Type Here")
    smoking = st.number_input("smoking", min_value=0, max_value=1, key="smoking", placeholder="Type Here")
    drinking = st.number_input("drinking", min_value=0, max_value=1, key="drinking", placeholder="Type Here")
    alt = st.number_input("alt", min_value=80, max_value=180, key="alt", placeholder="Type Here")



result = ""
if st.button("Predict"):
    result = predict_note_authentication(age, bmi, fpg, ffpg, sbp, dbp, family_history, smoking, drinking, alt)

if result == 0:
    st.success('The output is: No gestation diabetes')
elif result == 1:
    st.success('The output is: Gestation diabetes')
else:
    st.success('Enter Input value')  # Handle other cases if needed

    
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main_':
    main()