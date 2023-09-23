# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import time


# loading the saved models

diabetes_model = pickle.load(open('C:\\Users\\asus\\OneDrive\\Documents\\sih\\Multiple_Disease_Prediction_System\\saved_models\\diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:\\Users\\asus\\OneDrive\\Documents\\sih\\Multiple_Disease_Prediction_System\\saved_models\\heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:\\Users\\asus\\OneDrive\\Documents\\sih\\Multiple_Disease_Prediction_System\\saved_models\\parkinsons_model.sav','rb'))


with st.sidebar:
    
    # css = """
    #     <style>
    #         #custom-option-menu{
    #             color: red;
    #         }
    #     </style>
    # """
    
    # st.markdown(css, unsafe_allow_html=True)
        
    # st.markdown('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">',unsafe_allow_html=True)
    
    selected = option_menu('Contents',
                          
                          ['Introduction',
                           'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson\'s Prediction',
                           'Depression'],
                          icons=['person','activity','heart','hospital','window'],
                          default_index=0,
                          key='custom-option-menu')

    

st.markdown("""
            <style>
            [data-testid="stSidebar"][aria-expanded="true"]{
            min-width: 400px;
            max-width: 400px;
            }
            </style>
            """,unsafe_allow_html=True,)
    
    
if(selected == 'Introduction'):
    html_code = """
        <h1>Welcome!</h1>
        <div class="type">
            This is a Disease Prediction Model made using several python libraries and deployed using streamlit.
        </div>
    """
    css_code = """
        <style>
            h1{
                font-size: 50px;
                color: #034644;
            }
            .type{
                font-weight: bold;
                font-size: 16px;
                overflow: hidden;
                white-space: nowrap;
                animation: typewriter 7s steps(100);
            }
            @keyframes typewriter{
                from {
                    width: 0; /* Start with zero width */
                }
                to{
                    width: 100%;
                }
            }
        </style>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    st.markdown(css_code, unsafe_allow_html=True)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinson's Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

if (selected == 'Depression'):
    html_code = """
        <h1>Hello!</h1>
        <h2>How are you feeling today? Feel Free to Connect with <a class="link" src="#">Jarvis</a>, our chatbot who is eager to talk to you!</h2>
        <div class="container">
            <div class="recieved">Hi. I'm feeling low.</div>
            <div class="sent">I can Help!</div>
        </div>
    """
    
    css_code = """
        <style>
            body{
                font-family: "HelveticaNeue-CondensedBold";
                font-weight: bold;
            }
            h1,h2{
                color: #034644;
            }
            h2{
                position: relative;
                top: -30px;
            }
            .container{
                margin-top: 30px;
                background-color: white;
                padding: 20px;
                border-radius: 20px;
            }
            .sent{
                margin-top: 15px;
                margin-left: 15px;
                border: 1px solid black;
                padding: 10px;
                border-radius: 7px;
                background-color: skyblue;
                width: fit-content;
                color: white;
            }
            .recieved{
                color: white;
                margin-top: 10px;
                border: 1px solid black;
                padding: 10px;
                border-radius: 7px;
                text-align: right;
                background-color: #034644;
                margin-bottom: 15px;
                width: fit-content;
                position: relative;
                left: 500px;
            }
            hover
            .sent .recieved{
                
            }
        </style>
    """
    st.markdown(html_code, unsafe_allow_html=True)
    st.markdown(css_code, unsafe_allow_html=True)