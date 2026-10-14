import streamlit as st
import plotly.express as px

# Set up the page
st.set_page_config(page_title="Global Inequality Dashboard", layout="wide")

st.title("🌍 Global Inequality Dashboard")
st.markdown("An Interactive Analysis by Muhammad Talha Ateeq")

# Use a reliable built-in dataset (Gapminder) about Global Inequality
df = px.data.gapminder()

# Create the Year Slider
year_filter = st.slider("Select Year", int(df.year.min()), int(df.year.max()), 2007)
filtered_df = df[df['year'] == year_filter]

# Create the scatter plot
fig = px.scatter(
    filtered_df,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
    title=f"GDP per Capita vs Life Expectancy ({year_filter})",
    template="plotly_dark"
)

# Show the chart
st.plotly_chart(fig, use_container_width=True)
