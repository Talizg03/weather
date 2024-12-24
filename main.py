import requests
import toml
import streamlit as st

with open('secret.toml','r') as f:
    config = toml.load(f)
# Function to fetch weather data
def get_weather(city_name, api_key):


    # Construct the URL for the API request
    complete_url = "http://api.weatherstack.com/current ? access_key=" + config['API'] +" & query=" + city_name
    # Send a GET request to the API
    response = requests.get(complete_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response into JSON format
        data = response.json()

        # Extract required data
        main_data = data['main']
        weather_data = data['weather'][0]

        # Extract temperature, pressure, humidity, and weather description
        temperature = main_data['temp']
        pressure = main_data['pressure']
        humidity = main_data['humidity']
        description = weather_data['description']

        return temperature, pressure, humidity, description
    else:
        # If city is not found or request fails
        return None


# Streamlit UI for input and display
def weather_app():
    st.title('Weather Prediction App')

    # Get the API key (replace with your own)
    api_key = 'YOUR_API_KEY_HERE'  # Replace this with your OpenWeatherMap API key

    # Input field for the city name
    city_name = st.text_input('Enter city name:', 'London')

    if city_name:
        # Get the weather data for the city
        weather_data = get_weather(city_name, api_key)

        if weather_data:
            temperature, pressure, humidity, description = weather_data

            # Display the weather data
            st.write(f"Weather for {city_name}:")
            st.write(f"Temperature: {temperature}°C")
            st.write(f"Pressure: {pressure} hPa")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Description: {description}")
        else:
            st.write("City not found or there was an error with the API request.")


# Run the Streamlit app
if __name__ == '__main__':
    weather_app()

