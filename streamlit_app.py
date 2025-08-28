import streamlit as st
from PIL import Image

st.title("Mi primera app")

img = Image.open("Assets/keko.png")

st.image(img, caption="DAMNNNNN")
