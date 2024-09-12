import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    # Load the dataset
    df = pd.read_csv('ElectricCarData_Clean.csv')

    # Streamlit app title
    st.title("Electric Car Data Visualization")

    col1,col2 = st.columns(2)
    # Distribution Plots

    with col1:
        #st.header("Distribution of Prices and Range")
        # Histogram for Price
        st.subheader("Histogram of Car Prices")
        fig, ax = plt.subplots()
        ax.hist(df['PriceEuro'], bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Price (Euro)')
        ax.set_ylabel('Number of Cars')
        ax.set_title('Distribution of Car Prices')
        st.pyplot(fig)

    with col2:
        # Histogram for Range
        st.subheader("Histogram of Car Range")
        fig, ax = plt.subplots()
        ax.hist(df['Range_Km'], bins=20, color='green', edgecolor='black')
        ax.set_xlabel('Range (Km)')
        ax.set_ylabel('Number of Cars')
        ax.set_title('Distribution of Car Range')
        st.pyplot(fig)


    col3,col4 = st.columns(2)


    with col3:
    # Bar Charts
    #    st.header("Brand Analysis")

        # Bar chart for Brand vs. Average Price
        st.subheader("Average Price by Brand")
        avg_price_per_brand = df.groupby('Brand')['PriceEuro'].mean().sort_values()
        fig, ax = plt.subplots(figsize=(10, 8))
        avg_price_per_brand.plot(kind='barh', color='orange', ax=ax)
        ax.set_xlabel('Average Price (Euro)')
        ax.set_ylabel('Brand')
        ax.set_title('Average Price of Cars by Brand')
        st.pyplot(fig)
    with col4:
    # Bar chart for Brand vs. Number of Models
        st.subheader("Number of Models per Brand")
        model_count_per_brand = df['Brand'].value_counts().sort_values()
        fig, ax = plt.subplots(figsize=(10, 8))
        model_count_per_brand.plot(kind='barh', color='purple', ax=ax)
        ax.set_xlabel('Number of Models')
        ax.set_ylabel('Brand')
        ax.set_title('Number of Models per Brand')
        st.pyplot(fig)


    col5,col6 = st.columns(2)
    with col5:
        # Scatter Plots
    #    st.header("Relationship Analysis")

        # Scatter plot for Range vs. Price
        st.subheader("Range vs. Price")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='Range_Km', y='PriceEuro', ax=ax)
        ax.set_xlabel('Range (Km)')
        ax.set_ylabel('Price (Euro)')
        ax.set_title('Range vs. Price')
        st.pyplot(fig)

    with col6:
    # Scatter plot for Acceleration vs. Price
        st.subheader("Acceleration vs. Price")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x='AccelSec', y='PriceEuro', ax=ax)
        ax.set_xlabel('Acceleration (0-100 km/h in seconds)')
        ax.set_ylabel('Price (Euro)')
        ax.set_title('Acceleration vs. Price')
        st.pyplot(fig)

    col7,col8 = st.columns(2)
    # Box Plots
    #st.header("Box Plot Analysis")
    with col7:
    # Box plot for Price by Segment
        st.subheader("Price Distribution by Segment")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.boxplot(x='Segment', y='PriceEuro', data=df, ax=ax)
        ax.set_xlabel('Segment')
        ax.set_ylabel('Price (Euro)')
        ax.set_title('Price Distribution by Segment')
        st.pyplot(fig)

    with col8:
    # Box plot for Efficiency by Body Style
        st.subheader("Efficiency by Body Style")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.boxplot(x='BodyStyle', y='Efficiency_WhKm', data=df, ax=ax)
        ax.set_xlabel('Body Style')
        ax.set_ylabel('Efficiency (Wh/Km)')
        ax.set_title('Efficiency by Body Style')
        st.pyplot(fig)

    col9,col10 = st.columns(2)

    with col9:
    # Pie Charts
    #st.header("Pie Charts")

        # Pie chart for Body Style distribution
        st.subheader("Distribution of Body Styles")
        body_style_counts = df['BodyStyle'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(body_style_counts, labels=body_style_counts.index, autopct='%1.1f%%', startangle=140)
        ax.set_title('Distribution of Body Styles')
        st.pyplot(fig)

    with col10:
    # Pie chart for PowerTrain distribution
        st.subheader("Distribution of PowerTrains")
        powertrain_counts = df['PowerTrain'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(powertrain_counts, labels=powertrain_counts.index, autopct='%1.1f%%', startangle=140)
        ax.set_title('Distribution of PowerTrains')
        st.pyplot(fig)

    # Heatmap
    st.header("Correlation Heatmap")

    # Correlation heatmap
    st.subheader("Heatmap of Numerical Features")
    correlation_matrix = df[['AccelSec', 'TopSpeed_KmH', 'Range_Km', 'Efficiency_WhKm', 'PriceEuro']].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)
