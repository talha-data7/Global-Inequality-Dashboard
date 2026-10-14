import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Global Inequality Dashboard", layout="wide")

st.title("🌍 Global Inequality Dashboard")
st.markdown("### An Interactive Analysis by Muhammad Talha Ateeq")

# Load data
url = 'https://raw.githubusercontent.com/talha-data7/Global-Inequality-Dashboard/main/world_happiness.csv'
df = pd.read_csv(url)

# Sidebar filter
st.sidebar.header("Filter Options")
score_filter = st.sidebar.slider("Minimum Happiness Score", 0.0, 10.0, 5.0)
filtered_df = df[df['Score'] >= score_filter]

# Create the chart
fig = px.scatter(
    filtered_df, 
    x='GDP per capita', 
    y='Healthy life expectancy', 
    size='Social support', 
    color='Score', 
    hover_name='Country or region',
    title='GDP per Capita vs Healthy Life Expectancy',
    template='plotly_white'
)

st.plotly_chart(fig, use_container_width=True)
