import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis apliaciones para interfaces multimodales")
st.write("Facilmente puedo realizar backend frontend.")
image = Image.open('imagen1.jpeg')

st.image(image, caption= 'Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es', texto)

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columnas(2)

with col1:
  st.subheader("Esta es la primera columna")
          
