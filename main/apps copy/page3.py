import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px


def app():

    uploaded_file = st.sidebar.file_uploader("Choose a File",type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)


        st.subheader("Original Data")
        st.dataframe(df)


        st.subheader("Electric Vehicle Range VS EV Brand")
        st.bar_chart(df,x="Brand",y="Range_Km")

    #    st.subheader("Fast Charge VS EV Brand")
    #    st.scatter_chart(
    #    df,
    #    x='Brand',
    #    y='FastCharge_KmH',
    #    color='Model',
    #    size='Range_Km',
    #)
        st.subheader("Fast Charge VS EV Brand")
        st.bar_chart(df,x="Brand",y="FastCharge_KmH")



        # Sorting data by the 'Score' column in descending order and taking the top 10
        top_10 = df.sort_values(by='FastCharge_KmH', ascending=False).head(10)

        # Displaying the top 10 data in Streamlit
        st.write("Top 10 Highest Fast Charge")
        st.dataframe(top_10)

        # Bar chart
        st.write("Top 10 Scores Bar Chart:")
        st.scatter_chart(top_10.set_index('Brand')['FastCharge_KmH'])


        range_df = df.sort_values(by=['Range_Km'], ascending=False)
        range_df= range_df[['Brand','Model','Range_Km']].head(n=1)
        st.table(range_df)


        fig = px.bar(df,x=df['Model'],y=df['Efficiency_WhKm'],animation_frame=df['Brand'])
        st.write(fig)

        fig1 = px.bar(df,x=df['Model'],y=df['PriceEuro'],animation_frame=df['Brand'])
        st.write(fig1)

        st.sidebar.subheader('Compare Data')
        sorted_brand = sorted(df.Brand.unique())
        selected_brand = st.sidebar.multiselect('Brand',sorted_brand,sorted_brand)

        sorted_range = sorted(df.Range_Km.unique())
        selected_range = st.sidebar.multiselect('Range',sorted_range,sorted_range)
        df_selected_brand = df[(df.Brand.isin(selected_brand))&(df.Range_Km.isin(selected_range))]



        st.header('Display Data')
        st.write('Data:'+str(df_selected_brand.shape[0])+'rows and'+ str(df_selected_brand.shape[1])+ ' columns.')
        st.dataframe(df_selected_brand)


        st.bar_chart(df_selected_brand,x="Brand",y="Range_Km",color="TopSpeed_KmH")

        st.sidebar.subheader('Filter Data')
        sorted_brand = sorted(df.Brand.unique())
        selected_brand = st.sidebar.multiselect('Brand',sorted_brand)

        st.sidebar.subheader('Efficiency Kilometer')
        sorted_km = sorted(df.Efficiency_WhKm.unique())
        selected_km = st.sidebar.multiselect('Efficiency Kilometer',sorted_km)

        df = df.sort_values(by='Brand',ascending=True)
        selected = st.multiselect('Select Brand',df.columns[1:],[df.columns[1]])

        st.write(df[['Brand']+selected].set_index('Brand'))

        fig = px.line(df,x='Brand',y=selected)

        st.write(fig)
