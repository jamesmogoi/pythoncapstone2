import streamlit as st
import plotly.express as px
from backend import get_forecast_data, get_current_weather

# Page configuration
st.set_page_config(page_title="Weather Forecast App", page_icon="🌤", layout="wide")

# App title
st.title("🌤 Weather Forecast App")

# User Input
place = st.text_input("🌍 Enter City Name:", placeholder="e.g., Nairobi")
days = st.slider("📅 Select Forecast Days", min_value=1, max_value=5, value=3)
option = st.selectbox("📊 Select Data to View:", ("Temperature", "Sky Condition"))

# Display current weather if a place is entered
if place:
    current_weather = get_current_weather(place)

    if current_weather:
        st.subheader(f"📍 Current Weather in {place}")
        cols = st.columns(4)

        with cols[0]:
            st.metric("Temperature", f"{current_weather['temperature']}°C")
        with cols[1]:
            st.metric("Humidity", f"{current_weather['humidity']}%")
        with cols[2]:
            st.metric("Wind Speed", f"{current_weather['wind_speed']} m/s")
        with cols[3]:
            icon_url = f"https://openweathermap.org/img/wn/{current_weather['icon']}@2x.png"
            st.image(icon_url, caption=current_weather["weather"].capitalize(), width=100)

        # Get and display forecast data
        forecast_data = get_forecast_data(place, days)

        if forecast_data:
            st.subheader(f"{option} Forecast for Next {days} Days")

            if option == "Temperature":
                temperatures = [entry["main"]["temp"] for entry in forecast_data]
                dates = [entry["dt_txt"] for entry in forecast_data]

                fig = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"}, title="Temperature Trend")
                fig.update_layout(title_x=0.5, title_font_size=20, xaxis_title_font_size=14, yaxis_title_font_size=14)
                st.plotly_chart(fig, use_container_width=True)

            elif option == "Sky Condition":
                st.markdown("### ☁️ Sky Conditions Forecast")
                for i in range(0, len(forecast_data), 2):  # Show every other forecast
                    col1, col2 = st.columns([1, 3])
                    entry = forecast_data[i]

                    with col1:
                        icon_url = f"https://openweathermap.org/img/wn/{entry['weather'][0]['icon']}@2x.png"
                        st.image(icon_url, width=100)

                    with col2:
                        st.markdown(f"**Time**: {entry['dt_txt']}  \n**Condition**: {entry['weather'][0]['description'].capitalize()}  \n**Temperature**: {entry['main']['temp']}°C")
                    st.divider()
        else:
            st.error("⚠️ Unable to fetch forecast data. Please check the city name or try again later.")
    else:
        st.error("⚠️ City not found. Please check the spelling and try again.")

# Footer
st.markdown("---\nMade with ❤️ using Streamlit and OpenWeather API | Designed by Mogoi")
