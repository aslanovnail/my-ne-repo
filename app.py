import streamlit as st
import pandas as pd

st.title("Car Sales App")

try:
    df = pd.read_csv("vehicles_us.csv")
    st.subheader("Preview of the dataset")
    st.write(df.head())
except FileNotFoundError:
    st.error("vehicles_us.csv not found. Please check the file is in the same folder as app.py.")