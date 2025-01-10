from datetime import datetime
import pytz
import requests

import streamlit as st


# Function to fetch weather data
def get_weather(city_name):
    api_key = 'e6affaa056e1b1f765c4716b941ae4e7'
    url = f"https://api.weatherstack.com/current?access_key={api_key}"
    url = f"https://api.weatherstack.com/forecast?access_key={api_key}"
    querystring = {"query": city_name,"forecast_days":7}

    # Send a GET request to the API
    current_response = requests.get(url,params=querystring)
    forecast_response = requests.get(url, params=querystring)

    # Check if the request was successful
    if current_response.status_code == 200 and forecast_response.status_code == 200:
        # Parse the responses into JSON format
        current_data = current_response.json()
        forecast_data = forecast_response.json()

        return current_data, forecast_data
    else:
        # If any of the requests fail
        return None, None


# Streamlit UI for input and display
def weather_app():
    st.title('Weather Prediction App')



    # Input field for the city name
    city_name = st.text_input('Enter city name: ')


    if city_name:
        # Get the weather data for the city
        current_data, forecast_data = get_weather(city_name)
        if current_data and forecast_data:
           current = current_data['current']
           location = current_data['location']
           forecast = forecast_data.get('forecast', {})
             # Display the weather data
           st.write(f"Weather for: {city_name}")
           st.write(f"Country:{location['country']}")
           st.write(f"Time of observation {datetime.now(pytz.timezone(location['timezone_id']))}")
           st.write(f"Temperature: {current['temperature']}°C")
           st.write(f"The weather description is:{", ".join(current['weather_descriptions'])}")
           if forecast:
                st.write(f"7-day Forecast:")
                for day, data in forecast.items():
                    st.write(f"{day}: {data['temperature']}°C, {', '.join(data['weather_descriptions'])}")
        else:
            st.write("City not found or there was an error with the API request.")



# Run the Streamlit app
if __name__ == '__main__':
    weather_app()

