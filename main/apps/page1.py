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
from vega_datasets import data
from folium.plugins import Fullscreen
import altair as alt


#st.header("Estimated Battery Lifetime")
st.set_page_config(page_title="Electric Vehicle Data Dashboard",layout="wide")


def app():

    # Sample data
    data = {
        'Month': ['January', 'February', 'March', 'April', 'May','June','July'],
        'Passenger_Vehicles': [2217, 2490, 2931, 3494, 3618,3997,4654]
    }

    df = pd.DataFrame(data)

    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May','June','July']

    # Convert 'Month' to a categorical type with the correct order
    df['Month'] = pd.Categorical(df['Month'], categories=month_order, ordered=True)

    # Custom color palette for the bars
    color_palette = ['#FF5733', '#1F77B4', '#2CA02C', '#FF7F0E', '#9467BD','#D62728','#17BECF']

    # Create a bar chart with custom colors
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('Month', sort=month_order),
        y='Passenger_Vehicles',
        color=alt.Color('Month', scale=alt.Scale(range=color_palette)),  # Apply custom color palette
        tooltip=['Month', 'Passenger_Vehicles']
    ).properties(
        title="Passenger Vehicles from January to July 2024"
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)

    data = {
        'Year': [1, 2, 3, 4, 5],
        'EVs_on_Road': [5308, 6446, 8459, 9686, 10778],
        'Passenger':[2217,2490,2931,3494,3618],
        'Cargo Light Truck':[11,12,15,17,18],
        '2-Wheeler':[2836,3704,5154,5806,6775],
        '3-Wheeler':[244,240,359,369,367],
        'Charging_Stations': [10, 30, 50, 80, 100],
        #'Carbon_Emissions_Reduced': [10, 25, 45, 70, 100], # in thousand tons
        'Renewable_Energy_Percentage': [0.1, 0.1, 0.1, 0.1, 0.03],
    }
    df = pd.DataFrame(data)


    col5, col6 = st.columns(2)

    with col5:


        st.header("Energy Mix in Charging Station")
        labels = ['Renewable', 'National-Grid']
        sizes = [df['Renewable_Energy_Percentage'].iloc[-1], 100 - df['Renewable_Energy_Percentage'].iloc[-1]]
        colors = ['#2ecc71', '#e74c3c']
        explode = (0.1, 0)  # explode 1st slice (i.e., 'Renewable')
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig1)


    with col6:

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


    data = {
        'EVs_on_Road': [66500],
        'Charging_Stations': [132],
    }
    df = pd.DataFrame(data)

# Bar chart using Altair
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('EVs_on_Road', title='EVs_on_Road'),
        y=alt.Y('Charging_Stations', title='Charging_Stations'),
        color='EVs_on_Road',  # Different color for each category
        tooltip=['EVs_on_Road', 'Charging_Stations']  # Hover tooltip for more info
    ).properties(
        title="Comparison of Charging Stations and Registered Cars"
    )

    # Display the chart
    #st.write("Comparison of Charging Stations and Registered Cars:")
    st.altair_chart(chart, use_container_width=True)


# Data
    data = {'Category': ['Charging Station', 'Registered Car'],
            'Value': [132, 66500]}

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create a bar chart
    chart = alt.Chart(df).mark_bar().encode(
        x='Category',
        y='Value',
        color='Category'
    )

    # Create a Streamlit app
    title="Comparison of Charging Station and Registered Car"
    st.altair_chart(chart, use_container_width=True)

    st.write("Ratio = Number of Charging Stations / Number of Registered Cars = 132 / 66500 = 0.002 or 1:505 (approximately) So, the ratio of charging stations to registered cars is approximately 1:505, meaning there is one charging station for every 505 electric vehicle.")
