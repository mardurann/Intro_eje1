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

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('CORRECTO')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ('Visual','Auditiva','Táctil'))
  if modo == 'Visual':
    st.write('La vista es fundamental para tu interfaz')
  if modo == 'Auditiva':
    st.write == ('La audición es fundamental para tu interfaz')
  if modo == 'Táctil':
    st.write == ('El tacto es fundamental para tu interfaz')

st.subheader("Uso de botones")
if st.button('Presione el botón'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')





          
