import requests  # Import the requests library to make HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
from ebooklib import epub  # Import the epub module from EbookLib for creating eBooks

def create_ebook(url, book_title):
    """Fetch content from a URL and create an EPUB eBook."""
    try:
        response = requests.get(url)  # Make a GET request to the specified URL
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Create a new EPUB book
        book = epub.EpubBook()
        book.set_title(book_title)  # Set the title of the book

        # Create a chapter with the parsed content
        chapter = epub.EpubHtml(title='Chapter 1', file_name='chap_01.xhtml')
        chapter.content = str(soup.prettify())  # Convert the soup object to a string

        # Add the chapter to the book
        book.add_item(chapter)

        # Define the spine (reading order) of the book
        book.spine = ['nav', chapter]

        # Write the EPUB file to disk
        epub.write_epub(f'{book_title}.epub', book, {})
        print(f'EPUB eBook "{book_title}.epub" created successfully.')

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
create_ebook('https://example.com/your-favorite-article', 'My eBook')