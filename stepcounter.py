import fitbit  # Import the Fitbit library to interact with the Fitbit API

def get_daily_steps(token):
    """
    Fetch the daily steps for a user from the Fitbit API.

    Parameters:
    token (str): The OAuth 2.0 access token for authenticating API requests.

    Returns:
    int: The number of steps taken today.
    """
    # Create a Fitbit client using the client ID, client secret, and OAuth token
    client = fitbit.Fitbit('client_id', 'client_secret', oauth2_token=token)
    
    # Call the activities endpoint to get the summary of activities
    steps = client.activities()['summary']['steps']
    
    # Return the number of steps from the summary
    return steps

# Call the function and print the number of steps today
# Replace 'your_token' with your actual OAuth 2.0 access token
print(f"Steps today: {get_daily_steps('your_token')}")