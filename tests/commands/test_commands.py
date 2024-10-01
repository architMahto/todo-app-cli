import unittest
from unittest import mock
from src.commands.commands import parse_user_command, execute_user_command
from src.commands.exceptions import UnknownCommandException

class TestCommands(unittest.TestCase):
    def test_parse_user_command_with_command_arg(self):
        with (
            mock.patch("src.clients.fileio.FileIoClient.add_entry"),
            mock.patch("builtins.input", return_value="add Learn Rust") as mock_input
        ):
            command_name, command_arg = parse_user_command()
            mock_input.assert_called_once_with("Type add, show, edit, complete or exit: ")
            assert command_name == "add"
            assert command_arg == "Learn Rust"

    def test_parse_user_command_without_command_arg(self):
        with mock.patch("builtins.input", return_value="show") as mock_input:
            command_name, command_arg = parse_user_command()
            mock_input.assert_called_once_with("Type add, show, edit, complete or exit: ")
            assert command_name == "show"
            assert command_arg == ""

    def test_execute_user_command_with_command_arg(self):
        with (
            mock.patch("src.clients.fileio.FileIoClient.add_entry"),
            mock.patch("src.handlers.todos.add_todo") as mock_add_todo_handler
        ):
            execute_user_command("add", "Learn Rust")
            mock_add_todo_handler.assert_called_once_with("Learn Rust")

    def test_execute_user_command_without_command_arg(self):
        with mock.patch("src.handlers.todos.get_todos") as mock_get_todos_handler:
            execute_user_command("show", "")
            mock_get_todos_handler.assert_called_once()

    def test_execute_user_command_with_unknown_command_exception(self):
        with mock.patch("builtins.print") as mock_print:
            execute_user_command("pop", "4")
            self.assertRaises(UnknownCommandException)
            mock_print.assert_called_once()
            self.assertIsInstance(
                mock_print.call_args[0][0],
                UnknownCommandException
            )

    def test_execute_user_command_with_value_error(self):
        with mock.patch("builtins.print") as mock_print:
            execute_user_command("complete", "Learn Rust")
            mock_print.assert_called_once()
            self.assertIsInstance(
                mock_print.call_args[0][0],
                ValueError
            )

    def test_execute_user_command_with_index_error(self):
        with mock.patch("builtins.print") as mock_print:
            execute_user_command("complete", "100")
            mock_print.assert_called_once()
            self.assertIsInstance(
                mock_print.call_args[0][0],
                IndexError
            )

    def test_execute_user_command_with_general_error(self):
        with (
            mock.patch(
                "src.clients.fileio.FileIoClient.get_data",
                side_effect=FileNotFoundError("[Errno 2] No such file or directory: \'data/todos.csv\'")
            ),
            mock.patch("builtins.print") as mock_print
        ):
            execute_user_command("show", "")
            mock_print.assert_called_once_with("Something went wrong. Please try again later")
