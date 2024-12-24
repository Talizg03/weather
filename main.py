from datetime import datetime
from os import write

import requests
import streamlit as st


# Function to fetch weather data
def get_weather(city_name):
    api_key = 'e6affaa056e1b1f765c4716b941ae4e7'
    url = f"https://api.weatherstack.com/current?access_key={api_key}"
    querystring = {"query": city_name}

    # Send a GET request to the API
    response = requests.get(url,params=querystring)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response into JSON format
        data = response.json()

        # Extract required data
        # main_data = data['main']
        # weather_data = data['weather'][0]
        #
        # # Extract temperature, pressure, humidity, and weather description
        # temperature = main_data['temp']
        # pressure = main_data['pressure']
        # humidity = main_data['humidity']
        # description = weather_data['description']

        return data["current"]
    else:
        # If city is not found or request fails
        return None


# Streamlit UI for input and display
def weather_app():
    st.title('Weather Prediction App')

    # Get the API key (replace with your own)
      # Replace this with your OpenWeatherMap API key

    # Input field for the city name
    city_name = st.text_input('Enter city name:', 'London')

    if city_name:
        # Get the weather data for the city
        weather_data = get_weather(city_name)

        if weather_data:
            # Display the weather data
            st.write(f"Weather for {city_name}:")
            st.write(f"Time of observation {datetime.now()}:")
            st.write(f"Temperature: {weather_data['temperature']}°C")
        else:
            st.write("City not found or there was an error with the API request.")


# Run the Streamlit app
if __name__ == '__main__':
    weather_app()

