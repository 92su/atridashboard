import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px
from vega_datasets import data


def app():

    st.sidebar.subheader('Choose a File')
    uploaded_file = st.sidebar.file_uploader("Choose a File",type="xlsx")
    if uploaded_file:
        df = pd.read_excel(uploaded_file,sheet_name=0)
        st.dataframe(df)

        st.subheader("Number of Electric Vehicle Registration")
        st.bar_chart(df,x="Vehicle_Type",y="January_2024")
        source = data.barley()


        st.subheader("Number of Electric Vehicle Registration")
        st.bar_chart(df,x="Vehicle_Type",y="February_2024")
        source = data.barley()
        #st.bar_chart(source, x="variety", y="yield", color="site", horizontal=True)


        st.subheader("Model with Highest Range")
        range_df = df.sort_values(by=['Vehicle_Type'], ascending=False)
        range_df= range_df[['January_2024','February_2024','March_2024']].head(n=1)
        st.table(range_df)




        st.sidebar.subheader('Compare Data')
        sorted_vehicle = sorted(df.Vehicle_Type.unique())
        selected_vehicle = st.sidebar.multiselect('Vehicle_Type',sorted_vehicle,sorted_vehicle)


        df2 = pd.read_excel('/Users/sumonaung/Desktop/Paper_2/main/charging.xlsx')
        st.dataframe(df2)

        st.sidebar.subheader('Filter Region')
        sorted_region = sorted(df2.region.unique())
        selected_region = st.sidebar.multiselect('Region',sorted_region,sorted_region)

        sorted_charging = sorted(df2.quick_charging.unique())
        selected_charging = st.sidebar.multiselect('Charging',sorted_charging,sorted_charging)
        df_selected_region = df[(df2.region.isin(selected_vehicle))&(df2.region.isin(selected_region))]


        st.header('Display Data')
        st.write('Data:'+str(df_selected_region.shape[0])+'rows and'+ str(df_selected_region.shape[1])+ ' columns.')
        st.dataframe(df_selected_region)

    #    df_grouped = (df.groupby(by=["January_2024"]).count()[["January_2024"]].sort_values(by="January_2024"))
    #    pie_chart = px.pie(df_selected_region,title="Number of Region",values='January_2024',names='region')
    #    st.plotly_chart(pie_chart)
