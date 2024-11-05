import json
import os  # Import os to check if the file exists

def add_task(task):
    """
    Add a new task to the todo.json file.

    Parameters:
    task (str): The task to be added to the to-do list.
    """
    # Check if the input is valid
    if not isinstance(task, str) or not task.strip():
        raise ValueError("Task must be a non-empty string.")

    # Check if the file exists, if not, create it with an empty list
    if not os.path.exists('todo.json'):
        with open('todo.json', 'w') as file:
            json.dump([], file)  #