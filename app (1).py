import streamlit as st
import joblib

chitti=joblib.load('heartpatients.joblib')
st.title('Heart Disease Prediction')

st.markdown("### Input Data")

st.markdown("#### Personal Information")
age=st.number_input('Age', min_value=0, max_value=200, value=30, step=1)
bmi=st.number_input('Body Mass Index',min_value=10.00, max_value=60.00, value=22.50, step=0.1)

st.markdown("#### Lifestyle Factors")
cpd=st.number_input('The number of cigarettes smoked per day',min_value=0, max_value=100, step=1)

st.markdown("#### Medical History & Vital Signs")
tcl=st.number_input('Total cholesterol level (mg/dL)',min_value=100.00, max_value=500.00, value=200.00, step=0.1)
sbp=st.number_input('Systolic blood pressure (mmHg)',min_value=70, max_value=300, value=120, step=1)
dbp=st.number_input('Diastolic blood pressure (mmHg)',min_value=40, max_value=180, value=80, step=1)
hr=st.number_input('Heart rate (bpm)',min_value=30, max_value=220, value=72, step=1)
gl=st.number_input('Glucose level (mg/dL)',min_value=50.00, max_value=600.00, value=90.00, step=0.1)

if st.button('TenYearCHD'):
    f=chitti.predict([[age,cpd,tcl,sbp,dbp,bmi,hr,gl]])
    if f==1:
        st.error('⚠️ There are some chances that you might get Heart Disease in next 10 years. So, Consult a Doctor and start taking precautions.')
    elif f==0:
        st.success('✅ You are Very Healthy')



st.write("---")

st.markdown("### Developed by **Sanka Vamsi Akshay**")

st.markdown(
    """
    📌 [GitHub](https://github.com/Sanka-Vamsi-Akshay)  |  
    💼 [LinkedIn](https://www.linkedin.com/in/sanka-vamsi-akshay-232276291)  |  
    📧 [Email](mailto:sankavamsiakshay@gmail.com)  
    """
)

st.markdown(
    "📜 This project is open-source under the [MIT License](https://opensource.org/licenses/MIT). You are welcome to use and modify it! "
    "If you find it helpful, please give credit to **Sanka Vamsi Akshay**. 😊"
)
