import streamlit as st

st.title("Mi primera aplicacion en python")

st.sidebar.title("Parametros")

st.write("Elaborado por jmoss")

st.sidebar.image("DMC.png")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"] )
