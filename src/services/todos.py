"""This module contains service methods for managing todos"""

from src.clients.fileio import FileIoClient

TODOS_FILE = "data/todos.txt"
todos_file_io_client = FileIoClient(TODOS_FILE)


def get_todos():
    """This method retrieves all todos"""
    todos = todos_file_io_client.get_data()
    return todos


def add_todo(entry):
    """This method adds a todo"""
    todos_file_io_client.add_entry(entry)


def edit_todo(entry_index, updated_entry_value):
    """This method edits a todo"""
    todos_file_io_client.edit_entry(entry_index, updated_entry_value)


def complete_todo(entry_index):
    """This method completes and deletes a todo"""
    todos_file_io_client.delete_entry(entry_index)
