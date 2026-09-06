import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perfumes Dashboard", layout="wide")

st.title("Perfumes Dashboard")
st.subheader("Análisis y visualización del catálogo de fragancias")

df = pd.read_csv("perfumes.csv")

st.write("### Catálogo General")
st.dataframe(df)

col1, col2 = st.columns(2)

with col1:
    st.write("### Comparativa de Precios ($USD)")
    st.bar_chart(df.set_index("name")["price"])

with col2:
    st.write("### Calificación de Fragancias")
    st.bar_chart(df.set_index("name")["rating"])

st.caption("Desplegado con Docker")
