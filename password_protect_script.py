import getpass  # Import the getpass module to securely get user input
import hashlib  # Import hashlib for hashing passwords

# Predefined hashed password (for demonstration purposes)
# In practice, you would hash the password when setting it
hashed_password = hashlib.sha256(b'secret').hexdigest()

def check_password():
    """Check if the entered password matches the predefined hashed password."""
    for attempt in range(3):  # Allow up to 3 attempts
        password = getpass.getpass('Enter your password: ')  # Prompt for password
        # Hash the entered password
        hashed_attempt = hashlib.sha256(password.encode()).hexdigest()
        
        if hashed_attempt == hashed_password:  # Compare hashed values
            print('Access Granted')  # Print access granted message
            return True  # Return true if access is granted
        else:
            print('Access Denied')  # Print access denied message
            if attempt < 2:  # If not the last attempt
                print('Try again...')
    
    return False  # Return false if access is denied after 3 attempts

if __name__ == "__main__":
    if check_password():
        # Your protected code here
        print("Executing protected code...")