import streamlit as st
import plotly.express as px
from backend import get_data  # Ensure this function is correctly implemented

st.title("Weather Forecast for the Next Days")

# User Inputs
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} forecast for the next {days} days in {place}")

# Fetch Data
if place:
    data = get_data(place, days)  # Ensure get_data returns the correct format
    
    if option == "Temperature":
        dates, temperatures = zip(*data)  # Assuming data is a list of (date, temp) tuples
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
        st.plotly_chart(figure)
    
    elif option == "Sky":
        st.write("Displaying sky conditions is not yet implemented.")
