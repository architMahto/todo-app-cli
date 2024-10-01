import unittest
from unittest import mock
from src.clients.fileio import FileIoClient

class TestFileIoClient(unittest.TestCase):
    def setUp(self):
        self.filename = "data/todos.txt"
        self.todos_file_io_client = FileIoClient(self.filename)
        self.file_data = ["Learn Python", "Learn NodeJs", "Learn Golang"]
        self.read_data = "\n".join(self.file_data)

    def test_init(self):
        with (
          mock.patch("os.path.isfile", return_value=False),
          mock.patch("builtins.open") as mock_open
        ):
            mock_file_io_client = FileIoClient("data/todos.csv")
            mock_open.assert_called_once_with("data/todos.csv", "a", encoding="utf-8")

    def test_get_data_success(self):
        m = mock.mock_open(read_data=self.read_data)

        with mock.patch("builtins.open", new=m) as mocked_file:
            result = self.todos_file_io_client.get_data()
            mocked_file.assert_called_once_with(self.filename, "r", encoding="utf-8")
        self.assertEqual(self.file_data, result)

    def test_add_entry_success(self):
        m = mock.mock_open(read_data=self.read_data)

        with mock.patch("builtins.open", new=m) as mocked_file:
            entry = "Learn Rust"
            expected_content = "\n".join(["Learn Python", "Learn NodeJs", "Learn Golang", "Learn Rust"])
            self.todos_file_io_client.add_entry(entry)
            mocked_file.assert_called_once_with(self.filename, "r+", encoding="utf-8")
            mocked_file().truncate.assert_called_once_with(0)
            mocked_file().writelines.assert_called_once_with(expected_content)

    def test_edit_entry_success(self):
        m = mock.mock_open(read_data=self.read_data)

        with mock.patch("builtins.open", new=m) as mocked_file:
            updated_entry_value = "Learn Rust"
            expected_content = "\n".join(["Learn Python", "Learn Rust", "Learn Golang"])
            self.todos_file_io_client.edit_entry(1, updated_entry_value)
            mocked_file.assert_called_once_with(self.filename, "r+", encoding="utf-8")
            mocked_file().truncate.assert_called_once_with(0)
            mocked_file().writelines.assert_called_once_with(expected_content)

    def test_edit_entry_error(self):
        m = mock.mock_open(read_data=self.read_data)

        with mock.patch("builtins.open", new=m) as mocked_file:
            updated_entry_value = "Learn Rust"
            self.assertRaises(IndexError, lambda:self.todos_file_io_client.edit_entry(7, updated_entry_value))
            self.assertRaises(IndexError, lambda:self.todos_file_io_client.edit_entry(-1, updated_entry_value))

    def test_delete_entry_success(self):
        m = mock.mock_open(read_data=self.read_data)

        with mock.patch("builtins.open", new=m) as mocked_file:
            expected_content = "\n".join(["Learn Python", "Learn Golang"])
            self.todos_file_io_client.delete_entry(1)
            mocked_file.assert_called_once_with(self.filename, "r+", encoding="utf-8")
            mocked_file().truncate.assert_called_once_with(0)
            mocked_file().seek.assert_called_once_with(0)
            mocked_file().writelines.assert_called_once_with(expected_content)

    def test_delete_entry_error(self):
        m = mock.mock_open(read_data=self.read_data)

        with mock.patch("builtins.open", new=m) as mocked_file:
            self.assertRaises(IndexError, lambda:self.todos_file_io_client.delete_entry(7))
            self.assertRaises(IndexError, lambda:self.todos_file_io_client.delete_entry(-1))


