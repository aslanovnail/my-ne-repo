import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    # Checkbox to exclude very expensive cars
exclude_expensive = st.checkbox('Exclude cars priced above $50,000')

# Filter data based on checkbox
if exclude_expensive:
    df = df[df['price'] <= 50000]
    st.markdown("*Note:* Very expensive cars (over $50,000) are excluded.")

# Histogram for 'price'
st.subheader('Price Distribution')
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['price'], bins=30, color='blue', edgecolor='black')
ax.set_title('Histogram of Car Prices')
ax.set_xlabel('Price')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Summary
avg_price = int(df['price'].mean())
st.markdown(f"*Average Price (after filter if applied):* ${avg_price:,}")