import unittest
from unittest import mock
from src.handlers.todos import display_todos, handle_add_todo, handle_get_todos, handle_edit_todo, handle_complete_todo

class TestTodosHandlers(unittest.TestCase):
    def setUp(self):
        self.todos = ["Learn Python", "Learn NodeJs", "Learn Golang"]
        self.expected_todos_after_edit = ["Learn Python", "Learn Rust", "Learn Golang"]

    def test_display_todos(self):
        with mock.patch("builtins.print") as mock_print:
            display_todos(self.todos)
            mock_print.assert_has_calls([
                mock.call("1. Learn Python"),
                mock.call("2. Learn NodeJs"),
                mock.call("3. Learn Golang")
            ])

    def test_handle_get_todos(self):
        with (
          mock.patch("src.handlers.todos.display_todos") as mock_display_todos,
          mock.patch("src.handlers.todos.get_todos", return_value=self.todos) as todos_service_get_todos
        ):
            handle_get_todos()
            todos_service_get_todos.assert_called_once()
            mock_display_todos.assert_called_once_with(self.todos)

    def test_handle_add_todo(self):
        with (
            mock.patch('src.clients.fileio.FileIoClient.add_entry'),
            mock.patch("src.handlers.todos.add_todo") as todos_service_add_todo
        ):
            handle_add_todo("Learn Rust")
            todos_service_add_todo.assert_called_with("Learn Rust")

    def test_handle_edit_todo(self):
        with (
            mock.patch("src.handlers.todos.get_todos", side_effect=[
                self.todos,
                self.expected_todos_after_edit
            ]),
            mock.patch("builtins.input", return_value="Learn Rust") as mock_input,
            mock.patch("src.handlers.todos.edit_todo") as todos_service_edit_todo
        ):
            handle_edit_todo("2")
            mock_input.assert_called_once_with("Enter new todo: ")
            todos_service_edit_todo.assert_called_with(1, "Learn Rust")

    def test_handle_complete_todo(self):
        with (
            mock.patch("src.handlers.todos.get_todos", return_value=self.todos) as todos_service_get_todos,
            mock.patch("src.handlers.todos.complete_todo") as todos_service_complete_todo,
            mock.patch("builtins.print") as mock_print
        ):
            handle_complete_todo("2")
            self.assertListEqual(todos_service_get_todos(), self.todos)
            todos_service_complete_todo.assert_called_with(1)
            mock_print.assert_called_once_with("Learn NodeJs was completed.")
