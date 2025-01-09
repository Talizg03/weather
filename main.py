from datetime import datetime
import pytz
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

        return data
    else:
        # If city is not found or request fails
        return None


# Streamlit UI for input and display
def weather_app():
    st.title('Weather Prediction App')



    # Input field for the city name
    city_name = st.text_input('Enter city name: ')


    if city_name:
        # Get the weather data for the city
        weather_data = get_weather(city_name)
        if weather_data:
            current = weather_data['current']
            location = weather_data['location']

            # Display the weather data
            st.write(f"Weather for: {city_name}")
            st.write(f"Country:{location['country']}")
            st.write(f"Time of observation {datetime.now(pytz.timezone(location['timezone_id']))}")
            st.write(f"Temperature: {current['temperature']}°C")
            st.write(f"The weather description is:{", ".join(current['weather_descriptions'])}")

        else:
            st.write("City not found or there was an error with the API request.")



# Run the Streamlit app
if __name__ == '__main__':
    weather_app()

