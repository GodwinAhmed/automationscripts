import psutil  # Import the psutil library for system and process utilities
import time  # Import the time module to manage time-related tasks

def monitor_cpu(interval=1):
    """Continuously monitor and print CPU and memory usage at specified intervals."""
    try:
        while True:  # Infinite loop for continuous monitoring
            cpu_usage = psutil.cpu_percent()  # Get CPU usage percentage
            memory_usage = psutil.virtual_memory().percent  # Get memory usage percentage
            print(f"CPU usage: {cpu_usage}% | Memory usage: {memory_usage}%")  # Print the usage
            time.sleep(interval)  # Wait for the specified interval before the next check
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")  # Graceful exit on keyboard interrupt

if __name__ == "__main__":
    monitor_cpu(interval=1)  # Call the function to start monitoring with a 1-second interval