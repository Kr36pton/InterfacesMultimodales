import streamlit as st
from PIL import Image

st.title("Mi primera app")

st.header("Pajaros patones. Más que las patas...")
st.write("el pajaro paton, la criatura más mistica, con más patas que pajaro, el pajaro patón")

img = Image.open("Assets/keko.png")

st.image(img, caption="DAMNNNNN")
