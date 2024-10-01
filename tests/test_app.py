import unittest
from unittest import mock
from src.app import app

class TestApp(unittest.TestCase):
  def test_app_with_exit_command(self):
    with (
       mock.patch("builtins.input", return_value="exit") as mock_input,
       mock.patch("builtins.print") as mock_print
    ):
        app()
        mock_input.assert_called_once_with("Type add, show, edit, complete or exit: ")
        mock_print.assert_called_once_with("Bye!")

  def test_app_with_successful_run(self):
    with (
       mock.patch("builtins.input", side_effect=[
          "show",
          "exit"
       ]) as mock_input,
       mock.patch("builtins.print") as mock_print
    ):
        app()
        self.assertEqual(mock_input.call_count, 2)
        self.assertEqual(mock_print.call_count, 5)
      #   mock_print.assert_called_once_with("Bye!")
