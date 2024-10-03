"""This module contains any custom exceptions"""


class UnknownCommandException(Exception):
    """This exception will be raised if a unprogrammed command is entered"""

    def __init__(self, message="You entered an unknown command"):
        super().__init__(message)
