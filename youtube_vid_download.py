import yt_dlp  # Import the yt-dlp library for downloading videos

def download_video(url):
    """Download a video from the provided URL."""
    # Options for yt-dlp
    ydl_opts = {
        'format': 'best',  # Download the best available quality
        'outtmpl': '%(title)s.%(ext)s',  # Set filename to video title
        'noplaylist': True,  # Download single video if URL is part of a playlist
        'quiet': False,  # Show download progress in the console
        'ignoreerrors': True,  # Continue even if an error is encountered
        'no_warnings': True,  # Suppress warnings
    }
    
    try:
        # Use yt-dlp to download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video from the provided URL
        print("Download completed successfully.")  # Success message
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any errors that occur

if __name__ == "__main__":
    video_url = input("Please enter the YouTube video URL: ")  # Prompt user for video URL
    download_video(video_url)  # Call the function with user input