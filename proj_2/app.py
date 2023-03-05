import streamlit as st
from PIL import Image
import webbrowser
font="Helvetica"
st.title("DATA VISUALIZATION APP")

image = Image.open('mine.jpg')
image2 = Image.open('sign.jpg')
col1, col2 = st.columns(2)
col1.image(image, caption=None, width=200, use_column_width=500, clamp=False, channels="RGB", output_format="auto")
url = 'https://www.linkedin.com/in/niharika-ginjupalli-835653204/'
btn_click = st.button("Click - INTRO")
if btn_click == True:
    col2.subheader("   Hi there!!! I am Niharika .""\n"
                 " So excited to be a part of this journey with "
                 "the like minded people , Under the guidence of INNOMATICS team . "
                 " I Have been experiencing the life of a data science student with hands on projects. "
                 "This is being first interesting productive work in data visualization and responsive data app development. "
                 "I am so much gratefull for this opputunity and particularly the teaching of KANAV BANSAL sir .""\n"
                 "Will get back to you with exciting works, See u After a little while ...")
    if col2.button('Connect with me on LinkedIn'):
        webbrowser.open_new_tab(url)
    col2.image(image2, caption=None, width=200, use_column_width=500, clamp=False, channels="RGB", output_format="auto")
    st.balloons()


