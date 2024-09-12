import streamlit as st
from st_vizzu import *
from multiapp import MultiApp
from ipyvizzu import Chart,Data, Config, Style,DisplayTarget
from streamlit.components.v1 import html
import pandas as pd
from apps import page1,page2,page3,page4
import ssl
from PIL import Image
ssl._create_default_https_context = ssl._create_unverified_context

#st.set_page_config(layout='wide',initial_sidebar_state='expanded')

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #008000;

    }
</style>
""", unsafe_allow_html=True)

with open ('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.image("pol.jpg", width=200)

app = MultiApp()

st.markdown("""
#  Automotive Technology Research Institute

""")
st.subheader(":car: Electric Vehicle Data Dashboard")

# Add all your application here
app.add_app("Home", page1.app)
app.add_app("Electric Vehicle Charging Station Infrastructure", page2.app)
app.add_app("Electric Vehicle Dataset", page3.app)
app.add_app("Data Visualization",page4.app)


app.run()
