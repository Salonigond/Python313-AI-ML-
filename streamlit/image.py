import streamlit as st
from PIL import Images

#Image from pillow
img=Image.open("streamlit.png")

#open the image file
st.image(img, width=200)
if st.checkbox("Show/Hide")
st.text("Showing the widget")
status= st.radio("Select Gender:",['Male','Female'])
if status == "Male":
st.success("Male")
else:
st.success("Female")