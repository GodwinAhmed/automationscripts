import requests  # Import the requests library to make HTTP requests

def is_website_online(url):
    """Check if a website is online."""
    try:
        response = requests.get(url, timeout=5)  # Set a timeout of 5 seconds
        return response.status_code == 200  # Return True if status code is 200 (OK)
    except requests.ConnectionError:
        print(f"Connection error while trying to reach {url}.")
        return False  # Return False if there's a connection error
    except requests.Timeout:
        print(f"Request to {url} timed out.")
        return False  # Return False if the request times out
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return False  # Return False for any other request-related errors

# Example usage
if __name__ == "__main__":
    url = 'https://example.com'
    if is_website_online(url):
        print(f"The website {url} is online.")
    else:
        print(f"The website {url} is offline.")
        