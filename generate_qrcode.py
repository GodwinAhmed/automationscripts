import qrcode  # Import the qrcode library for generating QR codes

def generate_qr(text, filename):
    """Generate a QR code and save it as a PNG file."""
    try:
        img = qrcode.make(text)  # Create a QR code image from the provided text
        img.save(f"{filename}.png")  # Save the image as a PNG file
        print(f"QR code generated and saved as '{filename}.png'")
    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

if __name__ == "__main__":
    generate_qr('https://example.com', 'my_qr_code')  # Generate a QR code for the URL