from PIL import Image  # Import the Image module from the PIL (Pillow) library for image processing
import os  # Import the os module for interacting with the operating system

def batch_resize(folder, width, height):
    """Resize all JPEG and PNG images in the specified folder to the given width and height."""
    # Iterate over each file in the specified folder
    for filename in os.listdir(folder):
        # Check if the file has a valid image extension
        if filename.endswith(('.jpeg', '.jpg', '.png')):
            # Open the image file
            img = Image.open(os.path.join(folder, filename))
            # Resize the image to the specified dimensions
            img = img.resize((width, height))
            # Save the resized image with a new filename prefix
            img.save(os.path.join(folder, f"resized_{filename}"))
            # Print a message indicating the image has been resized
            print(f'Resized {filename}')

# Call the function to resize images in the specified folder
batch_resize('/path/to/images', 800, 600)  # Replace with the actual path to the folder containing images