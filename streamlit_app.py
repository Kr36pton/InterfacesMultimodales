import streamlit as st
from PIL import Image

st.title("Mi primera app")

img = Image.open("InterfacesMultimodales/Assets/keko.png")

st.image(img, caption="DAMNNNNN")
