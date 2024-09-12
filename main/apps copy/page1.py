import streamlit as st
import numpy as np
import pandas as pd
import pdfkit
from datetime import date
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
from streamlit.components.v1 import iframe
import matplotlib.pyplot as plt
import folium
from streamlit_folium import st_folium
import seaborn as sns
import plotly.express as px

from folium.plugins import Fullscreen


#st.header("Estimated Battery Lifetime")
st.set_page_config(page_title="Automotive Technology Research Institute",layout="wide")

def app():

    data = {
        'Year': [1, 2, 3, 4, 5],
        'EVs_on_Road': [5308, 6446, 8459, 9686, 10778],
        'Passenger':[2217,2490,2931,3494,3618],
        'Cargo Light Truck':[11,12,15,17,18],
        '2-Wheeler':[2836,3704,5154,5806,6775],
        '3-Wheeler':[244,240,359,369,367],
        'Charging_Stations': [10, 30, 50, 80, 100],
        #'Carbon_Emissions_Reduced': [10, 25, 45, 70, 100], # in thousand tons
        'Renewable_Energy_Percentage': [0, 0, 4, 4, 4],
    }
    df = pd.DataFrame(data)


#    st.title("Automobile Technology Research Institute")
    st.title("Electric Vehicles Data Visualization - Myanmar")
    st.write("Explore the trends in electric vehicle adoption, charging infrastructure, and environmental impact in Myanmar.")

    col1, col2, col3,col4 = st.columns(4)

    with col1:
        st.header("Passenger")
        st.line_chart(df.set_index('Year')['Passenger'])
    with col2:
        st.header("CargoLightTruck")
        st.line_chart(df.set_index('Year')['Cargo Light Truck'])
    with col3:
        st.header("2-Wheeler")
        st.line_chart(df.set_index('Year')['2-Wheeler'])
    with col4:
        st.header("3-Wheeler")
        st.line_chart(df.set_index('Year')['3-Wheeler'])


    col5, col6, = st.columns(2)

    with col5:


        st.header("Energy Mix in 2023")
        labels = ['Renewable', 'Non-Renewable']
        sizes = [df['Renewable_Energy_Percentage'].iloc[-1], 100 - df['Renewable_Energy_Percentage'].iloc[-1]]
        colors = ['#2ecc71', '#e74c3c']
        explode = (0.1, 0)  # explode 1st slice (i.e., 'Renewable')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)


    with col6:

        #df = pd.DataFrame(
        #np.random.randn(1000, 2) / [25, 25] + [16.87131, 96.199379],
        #columns=['lat', 'lon'])
        #ax1.axis('equal')
        #st.map(df)



    #    some_location = {
    #        "lat": {
    #            "0": 16.87131,
    #        },
    #        "lon": {
    #            "0": 96.199379,
    #        },
    #    }

    #    st.map(some_location)

        some_location = {
            "lat": {
                "0": 17.006810481830172,
                "1": 17.0296569268228,
                "2": 17.0396640126007,
                "3": 16.9544676163641,
                "4": 17.0149826964073,
            },
            "lon": {
                "0": 96.1445324350728,
                "1": 96.1884778512453,
                "2": 96.1445325112582,
                "3": 96.1665039067113,
                "4": 96.1335453766807,
            },
        }

        st.map(some_location)


    #    m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
    #    folium.Marker( [39.949610, -75.150282]).add_to(m)
    #    Fullscreen(position="topleft").add_to(m)
    #    st_folium(m, height=500,width=500, returned_objects=[])

    #with col7:

    data = {
        'Year': [2023, 2024],
        'EVs_on_Road': [39374, 66500],
        'Charging_Stations': [119, 130],
    }
    df = pd.DataFrame(data)

    st.header("Correlation Between EV Adoption and Charging Infrastructure")
    fig2, ax1 = plt.subplots()
    sns.regplot(x=df['Charging_Stations'], y=df['EVs_on_Road'], ax=ax1)
    ax1.set_xlabel('Number of Charging Stations')
    ax1.set_ylabel('Number of EVs on the Road')
    ax1.set_title('EV Adoption vs. Charging Infrastructure')
    st.pyplot(fig2)
