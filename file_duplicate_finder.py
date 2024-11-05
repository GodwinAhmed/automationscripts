import os  # Import the os module for interacting with the operating system
import hashlib  # Import the hashlib module for hashing functions

def hash_file(filename):
    """Generate an MD5 hash for the specified file."""
    h = hashlib.md5()  # Create an MD5 hash object
    with open(filename, 'rb') as file:  # Open the file in binary read mode
        # Read the file in chunks to avoid using too much memory
        while chunk := file.read(8192):
            h.update(chunk)  # Update the hash object with the current chunk
    return h.hexdigest()  # Return the hexadecimal digest of the hash

def find_duplicates(folder):
    """Find and print duplicate files in the specified folder."""
    hashes = {}  # Dictionary to store file hashes and their corresponding file paths
    # Walk through the directory tree
    for dirpath, _, filenames in os.walk(folder):
        for f in filenames:
            full_path = os.path.join(dirpath, f)  # Create the full file path
            file_hash = hash_file(full_path)  # Generate the hash for the file
            # Check if the hash already exists in the dictionary
            if file_hash in hashes:
                # If it does, a duplicate is found; print the paths of the duplicates
                print(f"Duplicate found: {full_path} == {hashes[file_hash]}")
            else:
                # If not, store the hash and its corresponding file path
                hashes[file_hash] = full_path

# Call the function and specify the folder to search for duplicates
find_duplicates('/path/to/your/folder')  # Replace with the actual path to the folder you want to check