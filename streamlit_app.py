import streamlit as st
from PIL import image

st.title("Mi primera app")

image = image.opem("InterfacesMultimodales/Assets/keko.png")

st.image(image, caption="DAMNNNNN")
