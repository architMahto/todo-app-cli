import unittest
from unittest import mock
from src.services.todos import get_todos, add_todo, edit_todo, complete_todo

class TestTodosService(unittest.TestCase):
    def setUp(self):
        self.todos = ["Learn Python", "Learn NodeJs", "Learn Golang"]

    def test_get_todos_success(self):
      with mock.patch('src.clients.fileio.FileIoClient.get_data', return_value=self.todos) as file_io_get_data:
        result = get_todos()
        file_io_get_data.assert_called_once()
        self.assertEqual(self.todos, result)

    def test_add_todo_success(self):
      entry = "Learn Rust"
      with mock.patch('src.clients.fileio.FileIoClient.add_entry') as file_io_add_entry:
        add_todo(entry)
        file_io_add_entry.assert_called_once_with(entry)

    def test_edit_todo_success(self):
      updated_entry_value = "Learn Rust"
      with mock.patch('src.clients.fileio.FileIoClient.edit_entry') as file_io_edit_entry:
        edit_todo(1, updated_entry_value)
        file_io_edit_entry.assert_called_once_with(1, updated_entry_value)

    def test_complete_todo_success(self):
      with mock.patch('src.clients.fileio.FileIoClient.delete_entry') as file_io_delete_entry:
        complete_todo(1)
        file_io_delete_entry.assert_called_once_with(1)

