# import numpy as np
# import pickle
# import pandas as pd
# #from flasgger import Swagger
# import streamlit as st 

# from PIL import Image

# #app=Flask(__name__)
# #Swagger(app)

# pickle_in = open("classifier.pkl","rb")
# classifier=pickle.load(pickle_in)

# #@app.route('/')
# def welcome():
#     return "Welcome All"

# #@app.route('/predict',methods=["Get"])
# def predict_note_authentication(variance,skewness,curtosis,entropy):
    
#     """Let's Authenticate the Banks Note 
#     This is using docstrings for specifications.
#     ---
#     parameters:  
#       - name: variance
#         in: query
#         type: number
#         required: true
#       - name: skewness
#         in: query
#         type: number
#         required: true
#       - name: curtosis
#         in: query
#         type: number
#         required: true
#       - name: entropy
#         in: query
#         type: number
#         required: true
#     responses:
#         200:
#             description: The output values
        
#     """
   
#     prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
#     print(prediction)
#     return prediction



# def main():
#     st.title("Bank Authenticator")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     variance = st.text_input("Variance","Type Here")
#     skewness = st.text_input("skewness","Type Here")
#     curtosis = st.text_input("curtosis","Type Here")
#     entropy = st.text_input("entropy","Type Here")
#     result=""
#     if st.button("Predict"):
#         result=predict_note_authentication(variance,skewness,curtosis,entropy)
#     st.success('The output is {}'.format(result))
#     if st.button("About"):
#         st.text("Lets LEarn")
#         st.text("Built with Streamlit")

# if __name__=='__main__':
#     main()










# import streamlit as st
# import pickle

# # Load the pre-trained model
# pickle_in = open("classifier.pkl", "rb")
# svc = pickle.load(pickle_in)

# def predict_note_authentication(age, diabetes_duration, diabetic_retinopathy, smoking, drinking, height, weight, bmi, sbp, dbp, hba1c, fbg, tg, c_peptide, tc, hdlc, ldlc, insulin, metformin, lipid_lowering_drugs):
#     """Function to predict disease"""
#     prediction = svc.predict([[age, diabetes_duration, diabetic_retinopathy, smoking, drinking, height, weight, bmi, sbp, dbp, hba1c, fbg, tg, c_peptide, tc, hdlc, ldlc, insulin, metformin, lipid_lowering_drugs]])
#     return prediction[0]

# def main():
#     st.title("Gest Dia")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp, unsafe_allow_html=True)

#     # Input fields with validation
#     age = st.number_input("Age", min_value=1, max_value=120, key="age", help="Enter age")
#     diabetes_duration = st.number_input("Diabetes duration (y)", min_value=0, max_value=50, key="diabetes_duration", help="Enter diabetes duration")
#     diabetic_retinopathy = st.number_input("Diabetic retinopathy (DR)", min_value=0, max_value=1, key="diabetic_retinopathy", help="Enter 1 if present, 0 otherwise")
#     smoking = st.number_input("Smoking", min_value=0, max_value=1, key="smoking", help="Enter 1 if smoking, 0 otherwise")
#     drinking = st.number_input("Drinking", min_value=0, max_value=1, key="drinking", help="Enter 1 if drinking, 0 otherwise")
#     height = st.number_input("Height(cm)", min_value=50, max_value=250, key="height", help="Enter height in centimeters")
#     weight = st.number_input("Weight(kg)", min_value=10, max_value=500, key="weight", help="Enter weight in kilograms")
#     bmi = st.number_input("BMI (kg/m2)", min_value=10.0, max_value=100.0, key="bmi", help="Enter BMI")
#     sbp = st.number_input("SBP (mmHg)", min_value=50, max_value=250, key="sbp", help="Enter systolic blood pressure")
#     dbp = st.number_input("DBP (mmHg)", min_value=30, max_value=150, key="dbp", help="Enter diastolic blood pressure")
#     hba1c = st.number_input("HbA1c (%)", min_value=1.0, max_value=20.0, key="hba1c", help="Enter HbA1c level")
#     fbg = st.number_input("FBG (mmol/L)", min_value=1.0, max_value=20.0, key="fbg", help="Enter fasting blood glucose level")
#     tg = st.number_input("TG (mmol/L)", min_value=0.1, max_value=10.0, key="tg", help="Enter triglyceride level")
#     c_peptide = st.number_input("C-peptide (ng/ml)", min_value=0.1, max_value=10.0, key="c_peptide", help="Enter C-peptide level")
#     tc = st.number_input("TC (mmol/L)", min_value=1.0, max_value=10.0, key="tc", help="Enter total cholesterol level")
#     hdlc = st.number_input("HDLC (mmol/L)", min_value=0.1, max_value=5.0, key="hdlc", help="Enter HDL cholesterol level")
#     ldlc = st.number_input("LDLC (mmol/L)", min_value=0.1, max_value=5.0, key="ldlc", help="Enter LDL cholesterol level")
#     insulin = st.number_input("Insulin", min_value=0, max_value=1, key="insulin", help="Enter 1 if using insulin, 0 otherwise")
#     metformin = st.number_input("Metformin", min_value=0, max_value=1, key="metformin", help="Enter 1 if using metformin, 0 otherwise")
#     lipid_lowering_drugs = st.number_input("Lipid lowering drugs", min_value=0, max_value=1, key="lipid_lowering_drugs", help="Enter 1 if using lipid lowering drugs, 0 otherwise")

#     result = ""
    
#     # Check if any input field is empty
#     if st.button("Predict"):
#         if not all([age, diabetes_duration, diabetic_retinopathy, smoking, drinking, height, weight, bmi, sbp, dbp, hba1c, fbg, tg, c_peptide, tc, hdlc, ldlc, insulin, metformin, lipid_lowering_drugs]):
#             st.error("Please enter values for all input fields.")
#         else:
#             result = predict_note_authentication(float(age), float(diabetes_duration), float(diabetic_retinopathy), float(smoking), float(drinking), float(height), float(weight), float(bmi), float(sbp), float(dbp), float(hba1c), float(fbg), float(tg), float(c_peptide), float(tc), float(hdlc), float(ldlc), float(insulin), float(metformin), float(lipid_lowering_drugs))
#             st.success('The output is {}'.format(result))

#     if st.button("About"):
#         st.text("Lets Learn")
#         st.text("Built with Streamlit")

# if __name__ == '__main__':
#     main()
