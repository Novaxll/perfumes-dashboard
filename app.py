import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perfumes Dashboard", layout="wide")

st.title("Perfumes Dashboard")
st.subheader("Análisis y visualización del catálogo de fragancias")

df = pd.read_csv("perfumes.csv")

st.header("Catálogo General")
st.dataframe(df, use_container_width=True)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Comparativa de Precios ($USD)")
    st.bar_chart(df.head(20).set_index("name")["price"])

with col2:
    st.subheader("Calificación de Fragancias")
    st.bar_chart(df.head(20).set_index("name")["rating"])

st.markdown("---")
st.header("Análisis Avanzado")

col3, col4, col5 = st.columns(3)

with col3:
    st.subheader("Precio Promedio por Marca")
    avg_price = df.groupby("brand")["price"].mean().sort_values(ascending=False).head(10)
    st.bar_chart(avg_price)

with col4:
    st.subheader("Distribución por Género")
    gender_counts = df["gender"].value_counts()
    st.bar_chart(gender_counts)

with col5:
    st.subheader("Relación Precio vs. Calificación")
    st.scatter_chart(df, x="price", y="rating", color="gender")
