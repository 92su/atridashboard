import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
from vega_datasets import data
import altair as alt


def app():



    # Define the data
    data = {
        "Region": ["Nay Pyi Taw", "Yangon", "Mandalay", "Bago", "Ayeyarwady", "Mon", "Shan", "Magway", "Rakhine", "Sagaing", "Tanintharyi", "Kachin", "Kayah", "Kayin", "Chin"],
        "Quick Charging": [9, 25, 10, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Normal Charging": [0, 24, 11, 5, 12, 3, 6, 1, 1, 0, 0, 0, 0, 0, 0]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create a Streamlit app
    st.title("Charging Stations in Myanmar")

    # Bar chart for quick charging stations
    st.subheader("Quick Charging Stations by Region")
    quick_charging_chart = alt.Chart(df).mark_bar().encode(
        x="Region",
        y="Quick Charging",
        tooltip=["Region", "Quick Charging"]
    )
    st.altair_chart(quick_charging_chart, use_container_width=True)

    # Bar chart for normal charging stations
    st.subheader("Normal Charging Stations by Region")
    normal_charging_chart = alt.Chart(df).mark_bar().encode(
        x="Region",
        y="Normal Charging",
        tooltip=["Region", "Normal Charging"]
    )
    st.altair_chart(normal_charging_chart, use_container_width=True)

    # Bar chart for total charging stations by region
    st.subheader("Total Charging Stations by Region")
    df["Total"] = df["Quick Charging"] + df["Normal Charging"]
    total_charging_chart = alt.Chart(df).mark_bar().encode(
        x="Region",
        y="Total",
        tooltip=["Region", "Total"]
    )
    st.altair_chart(total_charging_chart, use_container_width=True)

    # Bar chart for total charging stations by type
    st.subheader("Total Charging Stations by Type")
    total_quick = df["Quick Charging"].sum()
    total_normal = df["Normal Charging"].sum()
    type_data = pd.DataFrame({
        "Type": ["Quick Charging", "Normal Charging"],
        "Total": [total_quick, total_normal]
    })
    type_chart = alt.Chart(type_data).mark_bar().encode(
        x="Type",
        y="Total",
        tooltip=["Type", "Total"]
    )
    st.altair_chart(type_chart, use_container_width=True)



##########################


        # Create a region selection dropdown
#    region = st.selectbox("Select a region", df["Region"].unique())

    # Filter the data by the selected region
#    filtered_df = df[df["Region"] == region]

    # Bar chart for quick charging stations
#    st.subheader("Quick Charging Stations in {}".format(region))
#    quick_charging_chart = alt.Chart(filtered_df).mark_bar().encode(
#        x="Region",
#        y="Quick Charging",
#        tooltip=["Region", "Quick Charging"]
#    )
#    st.altair_chart(quick_charging_chart, use_container_width=True)

    # Bar chart for normal charging stations
#    st.subheader("Normal Charging Stations in {}".format(region))
#    normal_charging_chart = alt.Chart(filtered_df).mark_bar().encode(
#        x="Region",
#        y="Normal Charging",
#        tooltip=["Region", "Normal Charging"]
#    )
#    st.altair_chart(normal_charging_chart, use_container_width=True)

    # Bar chart for total charging stations by region
#    st.subheader("Total Charging Stations in {}".format(region))
#    filtered_df["Total"] = filtered_df["Quick Charging"] + filtered_df["Normal Charging"]
#    total_charging_chart = alt.Chart(filtered_df).mark_bar().encode(
#        x="Region",
#        y="Total",
#        tooltip=["Region", "Total"]
#    )
#    st.altair_chart(total_charging_chart, use_container_width=True)


################################

        # Create a region selection dropdown
    region = st.selectbox("Select a region", df["Region"].unique())

    # Filter the data by the selected region
    filtered_df = df[df["Region"] == region]

    # Create a row with three columns
    col1, col2, col3 = st.columns(3)

    # Bar chart for quick charging stations
    with col1:
        st.subheader("Quick Charging Stations in {}".format(region))
        quick_charging_chart = alt.Chart(filtered_df).mark_bar().encode(
            x="Region",
            y="Quick Charging",
            tooltip=["Region", "Quick Charging"]
        )
        st.altair_chart(quick_charging_chart, use_container_width=True)

    # Bar chart for normal charging stations
    with col2:
        st.subheader("Normal Charging Stations in {}".format(region))
        normal_charging_chart = alt.Chart(filtered_df).mark_bar().encode(
            x="Region",
            y="Normal Charging",
            tooltip=["Region", "Normal Charging"]
        )
        st.altair_chart(normal_charging_chart, use_container_width=True)

    # Bar chart for total charging stations by region
    with col3:
        st.subheader("Total Charging Stations in {}".format(region))
        filtered_df["Total"] = filtered_df["Quick Charging"] + filtered_df["Normal Charging"]
        total_charging_chart = alt.Chart(filtered_df).mark_bar().encode(
            x="Region",
            y="Total",
            tooltip=["Region", "Total"]
        )
        st.altair_chart(total_charging_chart, use_container_width=True)


    # Melt the data for layered chart
    melted_df = pd.melt(filtered_df, id_vars=["Region"], value_vars=["Quick Charging", "Normal Charging"], var_name="Type", value_name="Count")

    # Layered chart for quick and normal charging stations
    st.subheader("Charging Stations in {}".format(region))
    chart = alt.layer(
        alt.Chart(melted_df).mark_bar().encode(
            x="Region",
            y="Count",
            color="Type",
            tooltip=["Region", "Type", "Count"]
        )
    ).properties(width=800)
    st.altair_chart(chart, use_container_width=True)



    data = {
        "Region": ["Nay Pyi Taw", "Yangon", "Mandalay", "Bago", "Ayeyarwady", "Mon", "Shan", "Magway", "Rakhine", "Sagaing", "Tanintharyi", "Kachin", "Kayah", "Kayin", "Chin"],
        "Quick Charging": [9, 25, 10, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "Normal Charging": [0, 24, 11, 5, 12, 3, 6, 1, 1, 0, 0, 0, 0, 0, 0]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Create a Streamlit app
    st.title("Selected Charging Stations in Myanmar")

    # Create a region selection dropdown
    regions = st.multiselect("Select two regions to compare", df["Region"].unique(), default=["Yangon", "Mandalay"])

    # Create a charging type selection dropdown
    charging_types = st.multiselect("Select two charging types to compare", df.columns[1:], default=["Quick Charging", "Normal Charging"])

    # Filter the data by the selected regions
    filtered_df = df[df["Region"].isin(regions)]

    # Filter the data by the selected charging types
    filtered_df = filtered_df[["Region"] + charging_types]

    # Melt the data for bar chart
    melted_df = pd.melt(filtered_df, id_vars=["Region"], value_vars=charging_types, var_name="Type", value_name="Count")

    # Bar chart for comparing two regions and two charging types
    st.subheader("Comparison of Charging Stations in {} and {} ".format(regions[0], regions[1]))
    chart = alt.Chart(melted_df).mark_bar().encode(
        x="Region",
        y="Count",
        color="Type",
        column="Type",
        tooltip=["Region", "Type", "Count"]
    ).properties( autosize={"type": "fit", "contains": "padding"})  # Set the height of the chart
    st.altair_chart(chart, use_container_width=True)
