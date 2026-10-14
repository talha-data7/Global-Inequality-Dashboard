import streamlit as st
import pandas as pd
import plotly.express as px

# Set up the page
st.set_page_config(page_title="Global Inequality Dashboard", layout="wide")

st.title("🌍 Global Inequality Dashboard")
st.markdown("An Interactive Analysis by Muhammad Talha Ateeq")

# Load the data safely
@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/talha-data7/Global-Inequality-Dashboard/main/world_happiness.csv'
    df = pd.read_csv(url, on_bad_lines='skip')
    return df

try:
    df = load_data()

    # Automatically find the column that contains the word "Score"
    score_col = [col for col in df.columns if 'Score' in col][0]

    # Create the Slider
    score_filter = st.slider("Minimum Happiness Score", 0.0, 10.0, 5.0)
    
    # Filter the data based on the slider using the auto-detected column
    filtered_df = df[df[score_col] >= score_filter]

    # Create the scatter plot
    fig = px.scatter(
        filtered_df,
        x="GDP per capita",
        y="Healthy life expectancy",
        color=score_col,
        hover_name="Country or region",
        title="GDP per Capita vs Healthy Life Expectancy",
        template="plotly_dark"
    )

    # Show the chart
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Data loading error: {e}")
