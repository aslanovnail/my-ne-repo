
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
st.header("Car Sales Data Analysis")
df = pd.read_csv('/Users/nailaslanov/.vscode/car_sales/vehicles_us.csv')
st.write("Data Overview")
st.dataframe(df.head(10))
st.write("Data Description")
st.dataframe(df.describe())
fig = px.histogram(df, x='price', nbins=30, title='Price Distribution', color='condition')
st.plotly_chart(fig)
fig2 = px.scatter(df, x='price', y='type', title='Price vs Type')
st.plotly_chart(fig2)
if st.checkbox('Show odometer distribution'):
    fig3 = px.histogram(df, x='odometer', nbins=30, title='Odometerfind Distribution')
    st.plotly_chart(fig3)