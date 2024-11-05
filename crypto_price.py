import requests  # Import the requests library to make HTTP requests

def get_crypto_price(crypto):
    """Fetch the current price of the specified cryptocurrency."""
    url = f"https://api.coindesk.com/v1/bpi/currentprice/{crypto}.json"  # API endpoint
    try:
        response = requests.get(url)  # Send a GET request to the API
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        data = response.json()  # Parse the JSON response
        return data['bpi']['USD']['rate']  # Return the price in USD
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Print request error
    except KeyError:
        print("Error: Could not find the price data for the specified cryptocurrency.")
    return None  # Return None if an error occurs

# Example usage
if __name__ == "__main__":
    crypto_symbol = 'BTC'  # Specify the cryptocurrency symbol
    price = get_crypto_price(crypto_symbol)  # Fetch the price
    if price:
        print(f"The current price of {crypto_symbol} is ${price}.")
    else:
        print("Failed to retrieve the cryptocurrency price.")