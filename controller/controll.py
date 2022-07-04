import streamlit as st
from PIL import Image
icon=Image("imagen")
st.title("**Ingeniería de Producción**")

st.write("Esta aplicación tiene el objetivo de presentar"
         "información relacionada a los caudales"
         "de producción")
st.sidebar.title(":around_down_small:*Production* ")
uploaded_file= st.sidebar.file_uploader("Upload your csv file here")
st.sidebar.radio("pages", options=["Home", "Data", "Basic Calculations"])
streamlit run controll.py