import streamlit as st
import pandas as pd

st.title("Car Sales App")

try:
    df = pd.read_csv("vehicles_us.csv")
    st.subheader("Preview of the dataset")
    st.write(df.head())
except FileNotFoundError:
    st.error("vehicles_us.csv not found. Please check the file is in the same folder as app.py.")
    st.subheader('Price Distribution')
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=30, color='blue', alpha=0.7)
    plt.title('Price Distribution of Cars')
    plt.xlabel('Price')
    st.pyplot()
    st.subheader('Price vs Mileage')
    plt.figure(figsize=(10, 6))
    plt.scatter(df['odometer'], df['price'], alpha=0.5)
    plt.title('Price vs Mileage')
    plt.xlabel('Mileage')
    plt.ylabel('Price')
    st.pyplot()
    show_type =st.checkbox('Show Car Type')
    if show_type:
        st.subheader('Car Type Distribution')
        car_type_counts = df['type'].value_counts()
        plt.figure(figsize=(10, 6))
        plt.bar(car_type_counts.index, car_type_counts.values, color='orange', alpha=0.7)
        plt.title('Car Type Distribution')
        plt.xlabel('Car Type')
        plt.ylabel('Count')
        st.pyplot()
    else:
        st.write("Check the box to see the car type distribution.")