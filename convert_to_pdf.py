import PyPDF2  # Import the PyPDF2 library for PDF file handling
import os  # Import os for file path handling

def pdf_to_text(pdf_file):
    """Extract text from a PDF file."""
    if not os.path.isfile(pdf_file):  # Check if the PDF file exists
        raise FileNotFoundError(f"The file '{pdf_file}' does not exist.")
    
    text = ''  # Initialize an empty string to store the extracted text
    try:
        with open(pdf_file, 'rb') as file:  # Open the PDF file in binary mode
            reader = PyPDF2.PdfReader(file)  # Create a PdfReader object
            for page in reader.pages:  # Iterate through each page in the PDF
                page_text = page.extract_text()  # Extract text from the page
                if page_text:  # Check if text extraction was successful
                    text += page_text  # Append extracted text to the string
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
    
    return text  # Return the extracted text

if __name__ == "__main__":
    try:
        extracted_text = pdf_to_text('example.pdf')  # Call the function to extract text
        print(extracted_text)  # Print the extracted text
    except FileNotFoundError as fnf_error:
        print(fnf_error)  # Print file not found error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Print any other errors