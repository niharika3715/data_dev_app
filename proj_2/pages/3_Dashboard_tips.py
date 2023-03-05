import streamlit as st
from matplotlib import image
import plotly.express as px
import os
import pandas as pd
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest,"images","tips.jpg")
DATA_PATH = os.path.join(dir_of_interest,"data","tips.csv")
st.header("Dashborad-Tips Data")
img=image.imread(IMAGE_PATH)
st.image(img)
df=pd.read_csv(DATA_PATH)
st.dataframe(df)
days = st.selectbox("select the day : ", df['day'].unique())
col1, col2 = st.columns(2)
fig1=px.histogram(df[df['day']==days],x="tip")
col1.plotly_chart(fig1,use_container_width=True)
fig2=px.box(df[df['day']==days],y="tip")
col2.plotly_chart(fig2,use_container_width=True)

