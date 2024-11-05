import requests  # Import the requests library to make HTTP requests

def get_weather(city_name, api_key):
    """Fetch the current weather for a given city using OpenWeatherMap API."""
    # Construct the API endpoint URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"  # Using metric units for temperature in Celsius

    # Make a GET request to the API
    response = requests.get(complete_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        # Extract relevant information
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        # Print the weather information
        print(f"City: {city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {description.capitalize()}")
    else:
        print("City not found or API request failed.")

# Example usage
api_key = "YOUR_API_KEY"  # Replace with your actual API key
city_name = input("Enter city name: ")  # Prompt user for city name
get_weather(city_name, api_key)  # Call the function to get weather