"""This module contains validator methods for all todos"""


def validate_select_todo(func):
    """This method checks if the selected todo is a valid number"""

    def wrapper(*args):
        selected_todo_index = args[0]
        if selected_todo_index.isdigit():
            func(int(selected_todo_index) - 1)
        else:
            raise ValueError("Please enter a number")

    return wrapper
