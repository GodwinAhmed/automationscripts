import os  # Import the os module for interacting with the operating system
import shutil  # Import the shutil module for file operations like moving files

def organize_folder(folder):
    # Define a dictionary that maps folder names to their corresponding file extensions
    file_types = {
        'Images': ['.jpeg', '.jpg', '.png', '.gif'],  # Image file extensions
        'Videos': ['.mp4', '.avi', '.mov'],  # Video file extensions
        'Documents': ['.pdf', '.docx', '.txt'],  # Document file extensions
        'Archives': ['.zip', '.rar']  # Archive file extensions
    }

    # Iterate over each file in the specified folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)  # Create the full file path
        if os.path.isfile(file_path):  # Check if the path is a file
            ext = os.path.splitext(filename)[1].lower()  # Get the file extension and convert to lowercase
            # Check each folder type and its associated extensions
            for folder_name, extensions in file_types.items():
                if ext in extensions:  # If the file extension matches one of the defined types
                    target_folder = os.path.join(folder, folder_name)  # Create the target folder path
                    os.makedirs(target_folder, exist_ok=True)  # Create the folder if it doesn't exist
                    shutil.move(file_path, os.path.join(target_folder, filename))  # Move the file to the target folder
                    print(f'Moved {filename} to {folder_name}')  # Print a message indicating the move

# Call the function and specify the folder to organize
organize_folder('/path/to/Downloads')  # Replace with the actual path to the folder you want to organize