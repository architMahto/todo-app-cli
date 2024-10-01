"""This module exports a function to run the application"""

from src.commands.commands import Command, parse_user_command, execute_user_command
from src.commands.exceptions import UnknownCommandException


def app():
    """This method is used to run the application"""
    while True:
        command_name, command_arg = parse_user_command()

        if command_name != Command.EXIT.value:
            execute_user_command(command_name, command_arg)
        else:
            break

    print("Bye!")
