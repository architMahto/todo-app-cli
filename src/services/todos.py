from src.clients.fileio import FileIoClient

TODOS_FILE = "data/todos.txt"
todos_file_io_client = FileIoClient(TODOS_FILE)


def get_todos():
    todos = todos_file_io_client.get_data()
    return todos


def add_todo(entry):
    todos_file_io_client.add_entry(entry)


def edit_todo(entry_index, updated_entry_value):
    todos_file_io_client.edit_entry(entry_index, updated_entry_value)


def complete_todo(entry_index):
    todos_file_io_client.delete_entry(entry_index)
