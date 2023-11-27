
# ------------------------------------------------------------------------------
# import numpy as np
# import pickle
# import pandas as pd
# import streamlit as st

# pickle_in = open("classifier.pkl", "rb")
# classifier = pickle.load(pickle_in)

# def predict_diabetes_risk(sex, age, diabetes_duration, diabetic_retinopathy, smoking, drinking, height, weight, bmi, sbp, dbp, hba1c, fbG, tg, c_peptide, tc, hdLc, ldLc, insulin, metformin, lipid_lowering_drugs):
#     """
#     Predicts diabetes risk using the provided parameters.

#     Parameters:
#       - name: sex
#         in: query
#         type: number
#         required: true
#       - name: age
#         in: query
#         type: number
#         required: true
#       - name: diabetes_duration
#         in: query
#         type: number
#         required: true
#       - name: diabetic_retinopathy
#         in: query
#         type: number
#         required: true
#       - name: smoking
#         in: query
#         type: number
#         required: true
#       - name: drinking
#         in: query
#         type: number
#         required: true
#       - name: height
#         in: query
#         type: number
#         required: true
#       - name: weight
#         in: query
#         type: number
#         required: true
#       - name: bmi
#         in: query
#         type: number
#         required: true
#       - name: sbp
#         in: query
#         type: number
#         required: true

#     Responses:
#         200:
#             description: The output values
#     """
#     # Preprocess the input data if needed
#     # ...

#     # Make a prediction
#     prediction = classifier.predict([[sex, age, diabetes_duration, diabetic_retinopathy, smoking, drinking, height, weight, bmi, sbp, dbp, hba1c, fbG, tg, c_peptide, tc, hdLc, ldLc, insulin, metformin, lipid_lowering_drugs]])

#     return prediction

# def main():
#     st.title("Diabetes Risk Predictor")
#     html_temp = """
#     <div style="background-color:blue;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Diabetes Risk Predictor App </h2>
#     </div>
#     """
#     st.markdown(html_temp, unsafe_allow_html=True)

#     # Get input from the user
#     # sex = st.number_input("Sex",min_value=0, max_value=1,help="Enter 1 if male, 0 if female")
#     sex = st.number_input("Sex", min_value=0, max_value=1, help="Enter 1 if male, 0 if female",value=1)
#     age = st.number_input("Age", min_value=24, max_value=88, value=57)
#     diabetes_duration = st.number_input("Diabetes duration (y)", min_value=0, max_value=32, key="diabetes_duration", help="Enter diabetes duration",value=10)
#     diabetic_retinopathy = st.number_input("Diabetic Retinopathy", min_value=0, max_value=1, value=1)
#     smoking = st.number_input("Smoking", min_value=0, max_value=1,value=1)
#     drinking = st.number_input("Drinking", min_value=0, max_value=1,value=0)
#     height = st.number_input("Height (cm)", min_value=108, max_value=190,value=178)
#     weight = st.number_input("Weight (kg)", min_value=42.0, max_value=122.0,value=60.0)
#     bmi = st.number_input("BMI (kg/m2)", min_value=16.0, max_value=63.0,value=18.94)
#     sbp = st.number_input("SBP (mmHg)", min_value=92.0, max_value=218.0,value=101.0)
#     result = ""

#     if st.button("Predict"):
#         result = predict_diabetes_risk(sex, age, diabetes_duration, diabetic_retinopathy, smoking, drinking, height, weight, bmi, sbp, dbp, hba1c, fbG, tg, c_peptide, tc, hdLc, ldLc, insulin, metformin, lipid_lowering_drugs)

#     st.success('The predicted diabetes risk is {}'.format(result))
#------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in = open("diabetes.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_diabetes_risk(age, bmi, fpg, ffpg, sbp,dbp, family_history, smoking, drinking, alt):
    """
    Predicts diabetes risk using the provided parameters.

    Parameters:
      - name: age
        in: query
        type: number
        required: true
      - name: bmi
        in: query
        type: number
        required: true
      - name: fpg
        in: query
        type: number
        required: true
      - name: ffpg
        in: query
        type: number
        required: true
      - name: sbp
        in: query
        type: number
        required: true
      - name: dbp
        in: query
        type: number
        required: true
      - name: family_history
        in: query
        type: number
        required: true
      - name: smoking
        in: query
        type: number
        required: true
      - name: drinking
        in: query
        type: number
        required: true
      - name: alt
        in: query
        type: number
        required: true

    Responses:
        200:
            description: The output values
    """
    # Preprocess the input data if needed
    # ...

    # Make a prediction
    prediction = classifier.predict([[age, bmi, fpg, ffpg, sbp,dbp, family_history, smoking, drinking, alt]])

    return prediction

def main():
    st.title("Diabetes Risk Predictor")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:black;text-align:center;">Streamlit Diabetes Risk Predictor App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Get input from the user
    age = st.number_input("Age", min_value=22, max_value=93, value=44)
    bmi = st.number_input("BMI (kg/m2)", min_value=15.6, max_value=50.0, value=25.7)
    fpg = st.number_input("FPG", min_value=1.78, max_value=10.0, value=6.69,help="FPG (Fasting Plasma Glucose)")
    ffpg = st.number_input("FFPG", min_value=3.2, max_value=35.0, value=7.4,help="FFPG (Final Fasting Plasma Glucose)")
    sbp = st.number_input("SBP (mmHg)", min_value=72.0, max_value=218.0, value=105.0,help="SBP (Systolic Blood Pressure)")
    dbp = st.number_input("DBP",min_value=45,max_value=140,value=78,help="DBP (Diastolic Blood Pressure)")
    family_history = st.number_input("Family History", min_value=0, max_value=1, value=0)
    smoking = st.number_input("Smoking", min_value=1, max_value=3, value=3,help="Smoking Status: 1: Current Smoker, 2: Ever Smoker, 3: Never Smoker")
    drinking = st.number_input("Drinking", min_value=1, max_value=3, value=3,help="Drinking Status: 1: Current Drinker, 2: Ever Drinker, 3: Never Drinker")
    alt = st.number_input("ALT", min_value=4.5, max_value=440.0, value=48.0)
    result = ""

    if st.button("Predict"):
        result = predict_diabetes_risk(age, bmi, fpg, ffpg, sbp,dbp, family_history, smoking, drinking, alt)


    if result==1:
      st.success('Sorry! you are having chances of having diabetes')
    elif result==0:
      st.success('Bravo! you are not having chances of having diabetes')

if __name__ == '__main__':
    main()


# if __name__ == '__main__':
#     main()