import os


class FileIoClient:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(self.filename):
            open(self.filename, "a", encoding="utf-8").close()

    def __read_sanitized_data(self, file):
        data = file.readlines()
        sanitized_data = [entry.replace("\n", "") for entry in data]
        return sanitized_data

    def __write_data(self, file, data):
        file.truncate(0)
        file.seek(0)
        file.writelines("\n".join(data))

    def __validate_selection(self, index, data):
        if index >= len(data) or index < 0:
            raise IndexError("Please enter a valid todo number")

    def get_data(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return self.__read_sanitized_data(file)

    def add_entry(self, entry):
        with open(self.filename, "r+", encoding="utf-8") as file:
            sanitized_data = self.__read_sanitized_data(file)
            sanitized_data.append(entry)
            self.__write_data(file, sanitized_data)

    def edit_entry(self, entry_index, updated_entry_value):
        with open(self.filename, "r+", encoding="utf-8") as file:
            sanitized_data = self.__read_sanitized_data(file)
            self.__validate_selection(entry_index, sanitized_data)
            sanitized_data[entry_index] = updated_entry_value
            self.__write_data(file, sanitized_data)

    def delete_entry(self, entry_index):
        with open(self.filename, "r+", encoding="utf-8") as file:
            sanitized_data = self.__read_sanitized_data(file)
            self.__validate_selection(entry_index, sanitized_data)
            sanitized_data.pop(entry_index)
            self.__write_data(file, sanitized_data)
