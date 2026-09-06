import streamlit as st
import pandas as pd

st.set_page_config(page_title="Perfumes Dashboard", layout="wide")

st.title("Perfumes Dashboard")
st.subheader("Análisis y visualización interactiva del catálogo de fragancias")

df = pd.read_csv("perfumes.csv")

st.sidebar.header("Filtros de Búsqueda")

gender_filter = st.sidebar.multiselect(
    "Género:",
    options=df["gender"].unique(),
    default=df["gender"].unique()
)

brands_available = sorted(df["brand"].unique().tolist())
brand_filter = st.sidebar.multiselect(
    "Marcas:",
    options=brands_available,
    default=brands_available
)

search_query = st.sidebar.text_input("Buscar fragancia por nombre:")

filtered_df = df[
    (df["gender"].isin(gender_filter)) &
    (df["brand"].isin(brand_filter))
]

if search_query:
    filtered_df = filtered_df[filtered_df["name"].str.contains(search_query, case=False, na=False)]

m1, m2, m3 = st.columns(3)
m1.metric("Total Fragancias", len(filtered_df))
m2.metric("Precio Promedio ($USD)", f"${filtered_df['price'].mean():.2f}" if not filtered_df.empty else "$0")
m3.metric("Calificación Promedio", f"{filtered_df['rating'].mean():.2f} ⭐" if not filtered_df.empty else "0")

st.write("### Catálogo de Fragancias")
st.dataframe(filtered_df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.write("### Top 15 Fragancias por Precio ($USD)")
    if not filtered_df.empty:
        top_price = filtered_df.sort_values(by="price", ascending=False).head(15)
        st.bar_chart(top_price.set_index("name")["price"])
    else:
        st.info("No hay datos para mostrar.")

with col2:
    st.write("### Top 15 Fragancias Mejor Calificadas")
    if not filtered_df.empty:
        top_rating = filtered_df.sort_values(by="rating", ascending=False).head(15)
        st.bar_chart(top_rating.set_index("name")["rating"])
    else:
        st.info("No hay datos para mostrar.")

st.caption("Desplegado con Docker")
