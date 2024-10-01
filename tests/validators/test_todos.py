import unittest
from unittest import mock
from src.validators.todos import validate_select_todo

class TestTodosValidators(unittest.TestCase):
  def test_validate_select_todo(self):
    @validate_select_todo
    def fn(selected_todo_index):
     self.assertEqual(selected_todo_index, 1)

    fn("2")

  def test_validate_select_todo_raise_error(self):
    @validate_select_todo
    def fn(selected_todo_index):
      return

    self.assertRaises(ValueError, lambda:fn("Hello"))
