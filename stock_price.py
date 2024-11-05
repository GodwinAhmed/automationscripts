import requests  # Import the requests library for making HTTP requests

def get_stock_price(symbol):
    """Fetch the current stock price for a given symbol."""
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token=your_api_key"
    response = requests.get(url)  # Send a GET request to the API
    data = response.json()  # Parse the JSON response
    return data['c']  # Return the current price

# Fetch and print the stock price for Apple Inc. (AAPL)
print(get_stock_price('AAPL'))
