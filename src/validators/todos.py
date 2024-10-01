def validate_select_todo(func):
    def wrapper(*args):
        selected_todo_index = args[0]
        if selected_todo_index.isdigit():
            func(int(selected_todo_index) - 1)
        else:
            raise ValueError("Please enter a number")

    return wrapper
