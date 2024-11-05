import os  # Import the os module to interact with the operating system
import time  # Import the time module to manage time-related tasks

def check_downloads(downloads_path):
    """Monitor the downloads directory and shut down if empty."""
    while True:  # Infinite loop
        try:
            # Check if the downloads directory is empty
            if not os.listdir(downloads_path):
                print("The downloads directory is empty. Shutting down...")
                os.system("shutdown /s /t 1")  # Execute shutdown command (Windows)
            else:
                print("Downloads directory is not empty. Checking again in 60 seconds.")
        except FileNotFoundError:
            print(f"Error: The directory '{downloads_path}' does not exist.")
            break  # Exit the loop if the directory does not exist
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  # Exit the loop on unexpected errors

        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    downloads_path = input("Enter the path to your downloads directory: ")  # User input for directory path
    check_downloads(downloads_path)  # Call the function to start monitoring