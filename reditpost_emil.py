import smtplib  # Import the smtplib library for sending emails
import requests  # Import the requests library for making HTTP requests

def send_email(subject, body):
    """Send an email with the specified subject and body."""
    from_addr = 'your_email@example.com'  # Replace with your email address
    to_addr = 'your_email@example.com'  # Replace with the recipient email address
    msg = f"Subject: {subject}\n\n{body}"  # Format the email message

    # Connect to the Gmail SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade to a secure connection
        # Log in to the email account
        server.login('your_email@example.com', 'your_password')  # Replace with your email and password
        server.sendmail(from_addr, to_addr, msg)  # Send the email

def get_reddit_posts(subreddit):
    """Fetch the latest posts from the specified subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/new.json"  # Reddit API endpoint for new posts
    headers = {'User -agent': 'Mozilla/5.0'}  # Set a user-agent to avoid request rejection
    response = requests.get(url, headers=headers)  # Make the GET request
    data = response.json()  # Parse the JSON response
    # Extract and return the titles of the posts
    return [post['data']['title'] for post in data['data']['children']]

# Get the latest posts from the 'python' subreddit
posts = get_reddit_posts('python')

# Send an email with the latest Reddit posts
send_email('Latest Reddit Posts', '\n'.join(posts))