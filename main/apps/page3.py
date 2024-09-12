import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
import altair as alt

def app():

    uploaded_file = st.sidebar.file_uploader("Choose a File",type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.subheader("Original Data")
        st.dataframe(df)


        st.subheader("Electric Vehicle Range VS EV Brand")
        st.bar_chart(df,x="Brand",y="Range_Km")



        # Clean the data
        df['FastCharge_KmH'] = pd.to_numeric(df['FastCharge_KmH'], errors='coerce')  # Convert to numeric, invalid parsing will be NaN
        df_cleaned = df[['Brand', 'FastCharge_KmH']].dropna()  # Drop rows with NaN values

        # Group by brand and calculate the average FastCharge_KmH
        df_filtered = df_cleaned.groupby('Brand').mean().reset_index()

        # Bar chart using Altair
        bar_chart = alt.Chart(df_filtered).mark_bar().encode(
            x=alt.X('Brand', sort='-y', title="Brand"),
            y=alt.Y('FastCharge_KmH', title="Average FastCharge Speed (Km/H)"),
            color=alt.Color('Brand', legend=None),
            tooltip=['Brand', 'FastCharge_KmH']  # Add tooltips for interaction
        ).properties(
            title="Average Fast Charging Speed (Km/H) by Brand",
            width=700
        ).configure_axis(
            labelAngle=45  # Tilt x-axis labels for readability
        )

        # Display in Streamlit
        st.write("### Average Fast Charging Speed (Km/H) by Brand")
        st.altair_chart(bar_chart, use_container_width=True)




        # Clean the data
        df['FastCharge_KmH'] = pd.to_numeric(df['FastCharge_KmH'], errors='coerce')  # Convert to numeric
        df_cleaned = df[['Brand', 'Model', 'FastCharge_KmH']].dropna()  # Keep necessary columns and drop NaN values

        # Get the Top 10 models with highest FastCharge_KmH
        df_top10 = df_cleaned.nlargest(10, 'FastCharge_KmH')

        # Create a bar chart using Altair
        bar_chart = alt.Chart(df_top10).mark_bar().encode(
            y=alt.Y('Model', sort='-x', title="Car Model"),  # Sort by FastCharge in descending order
            x=alt.X('FastCharge_KmH', title="Fast Charge Speed (Km/H)"),
            color=alt.Color('Brand', legend=None),  # Color by brand
            tooltip=['Model', 'Brand', 'FastCharge_KmH']  # Tooltip with more details
        ).properties(
            #title="Top 10 Electric Cars with Highest Fast Charging Speed",
            width=700
        )

        # Display the bar chart in Streamlit
        st.write("### Top 10 Electric Cars with Highest Fast Charging Speed")
        st.altair_chart(bar_chart, use_container_width=True)



        st.sidebar.subheader('Compare Data')
        sorted_brand = sorted(df.Brand.unique())
        selected_brand = st.sidebar.multiselect('Brand',sorted_brand,sorted_brand)

        sorted_range = sorted(df.Range_Km.unique())
        selected_range = st.sidebar.multiselect('Range',sorted_range,sorted_range)
        df_selected_brand = df[(df.Brand.isin(selected_brand))&(df.Range_Km.isin(selected_range))]



        st.header('Display Data')
        st.write('Data:'+str(df_selected_brand.shape[0])+'rows and'+ str(df_selected_brand.shape[1])+ ' columns.')
        st.dataframe(df_selected_brand)


        st.bar_chart(df_selected_brand,x="Brand",y="AccelSec",color="TopSpeed_KmH")

    #    st.sidebar.subheader('Filter Data')
    #    sorted_brand = sorted(df.Brand.unique())
    #    selected_brand = st.sidebar.multiselect('Brand',sorted_brand)
#
#        st.sidebar.subheader('Efficiency Kilometer')
#        sorted_km = sorted(df.Efficiency_WhKm.unique())
#        selected_km = st.sidebar.multiselect('Efficiency Kilometer',sorted_km)
#
#        df = df.sort_values(by='Brand',ascending=True)
#        selected = st.multiselect('Select Brand',df.columns[1:],[df.columns[1]])

#        st.write(df[['Brand']+selected].set_index('Brand'))

#        fig = px.line(df,x='Brand',y=selected)

#        st.write(fig)
