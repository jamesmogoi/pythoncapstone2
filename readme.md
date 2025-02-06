# ☀️ Weather Forecast App

## Overview
The **Weather Forecast App** is a user-friendly web application built with **Streamlit** and **Plotly** that allows users to check current weather conditions and forecast data for any city worldwide. The app fetches real-time weather data using the **OpenWeather API**.

## Features
- **Current Weather Data**: Get live temperature, humidity, wind speed, and weather conditions for a given city.
- **Weather Forecast**: View temperature trends or sky conditions for up to 5 days.
- **Interactive Charts**: Visualize temperature changes with interactive **Plotly** charts.
- **User Input**: Enter a city name, select the forecast duration, and choose between temperature or sky conditions.
- **Minimalist UI**: Clean and intuitive interface designed using Streamlit.

## Technologies Used
- **Python** (Primary language)
- **Streamlit** (For web interface)
- **Plotly** (For interactive data visualization)
- **OpenWeather API** (For fetching weather data)
- **Requests** (For making API calls)
- **dotenv** (For managing API keys securely)

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/weather-forecast-app.git
cd weather-forecast-app
```

### 2. Create and Activate a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up OpenWeather API Key
- Sign up at [OpenWeather](https://openweathermap.org/) and get an API key.
- Create a **.env** file in the project root and add:
  ```ini
  OPENWEATHER_API_KEY=your_api_key_here
  ```

### 5. Run the Application
```sh
streamlit run app.py
```

## File Structure
```
weather-forecast-app/
│── backend.py       # Handles API calls to OpenWeather
│── app.py           # Main Streamlit application
│── .env             # Stores API key (ignored in .gitignore)
│── requirements.txt # Dependencies
│── README.md        # Documentation
```

## Usage
1. Enter a city name (e.g., **Nairobi**).
2. Select the number of forecast days (1-5).
3. Choose to view either **Temperature Trends** or **Sky Conditions**.
4. View interactive charts and weather icons for a visual representation.

## API & Data Handling
- The app interacts with OpenWeather’s **Current Weather API** and **5-day Forecast API**.
- Data is processed and visualized using **Plotly**.
- API requests are handled in **backend.py** for modularity.

## Improvements & Future Enhancements
- **Geolocation Support**: Auto-detect user’s location for convenience.
- **Hourly Forecast**: Allow users to view an hourly breakdown.
- **Caching**: Implement caching to optimize API calls.
- **Dark Mode**: UI theme switch for better user experience.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License
This project is licensed under the **MIT License**.

---

### 💙 Made with love using Streamlit & OpenWeather API

