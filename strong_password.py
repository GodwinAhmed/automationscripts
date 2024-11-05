import string
import secrets  # Import the secrets module for secure random numbers

def generate_password(length):
    """Generate a secure random password of specified length."""
    # Combine uppercase letters, lowercase letters, digits, and punctuation characters
    chars = string.ascii_letters + string.digits + string.punctuation
    # Generate a secure random password by selecting random characters from the combined string
    return ''.join(secrets.choice(chars) for _ in range(length))

# Generate and print a secure random password of length 16
print(generate_password(16))