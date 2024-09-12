import streamlit as st
import streamlit_authenticator as stauth
from st_vizzu import *
from multiapp import MultiApp
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget
from streamlit.components.v1 import html
import pandas as pd
from apps import page1, page2, page3, page4
import ssl
from PIL import Image
import pickle
from pathlib import Path
import time

# Set the session time limit (e.g., 30 minutes)
SESSION_TIME_LIMIT = 30 * 60  # in seconds

# user authentication
names = ["Peter Parker", "Rebecca Miller", "Su Mon Aung"]
usernames = ["pparker", "rmiller", "smaung"]

@st.cache_data
def load_hashed_passwords(file_path):
    with file_path.open("rb") as file:
        return pickle.load(file)

file_path = Path(__file__).parent / "hashed_pw.pkl"
hashed_passwords = load_hashed_passwords(file_path)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.session_state["authenticated"] = True
    st.session_state["username"] = username
    st.session_state["last_activity"] = time.time()

if st.session_state.get("authenticated", False):
    st.image("pol.jpg", width=200)
    st.write(f"Welcome, {name}!")
    # Add your application code here
    app = MultiApp()
    st.markdown("""
    #  Automotive Technology Research Institute

    """)
    st.subheader(":car: Electric Vehicle Data Dashboard")

    # Add all your application here
    app.add_app("Home", page1.app)
    app.add_app("Electric Vehicle Charging Station Infrastructure", page2.app)
    app.add_app("Electric Vehicle Dataset", page3.app)
    app.add_app("Data Visualization", page4.app)

    app.run()

    # Check if the session has expired
    if time.time() - st.session_state["last_activity"] > SESSION_TIME_LIMIT:
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.session_state["last_activity"] = None
        st.error("Session has expired. Please log in again.")

    # Add a logout button
    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = None
        st.session_state["last_activity"] = None
        st.error("You have been logged out. Please log in again.")
else:
    st.error("Invalid username or password")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
