"""This module contains constants, enums, and handler for a Command"""

from enum import Enum
from src.commands.exceptions import UnknownCommandException
from src.handlers.todos import (
    handle_add_todo,
    handle_complete_todo,
    handle_edit_todo,
    handle_get_todos,
)

Command = Enum(
    value="Command",
    names=[
        ("ADD", "add"),
        ("SHOW", "show"),
        ("EDIT", "edit"),
        ("COMPLETE", "complete"),
        ("EXIT", "exit"),
    ],
)

CommandHandlerMap = {
    Command.ADD.value: {"reqArgs": True, "handlerFn": handle_add_todo},
    Command.COMPLETE.value: {"reqArgs": True, "handlerFn": handle_complete_todo},
    Command.EDIT.value: {"reqArgs": True, "handlerFn": handle_edit_todo},
    Command.SHOW.value: {"reqArgs": False, "handlerFn": handle_get_todos},
}


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            command_name = args[0]
            if command_name not in Command._value2member_map_:
                raise UnknownCommandException("You entered an unknown command")
            func(*args, **kwargs)
        except UnknownCommandException as unknown_cmd_excp:
            print(unknown_cmd_excp)
        except ValueError as val_err:
            print(val_err)
        except IndexError as indx_err:
            print(indx_err)
        except Exception:
            print("Something went wrong. Please try again later")

    return wrapper


def parse_user_command():
    user_command = input("Type add, show, edit, complete or exit: ").strip()
    command_name, *command_arg = user_command.split(" ", 1)
    command_arg = command_arg[0] if command_arg else ""
    return command_name, command_arg


@handle_exceptions
def execute_user_command(command_name, command_arg):
    command_handler = CommandHandlerMap[command_name]
    if command_handler["reqArgs"]:
        command_handler["handlerFn"](command_arg)
    else:
        command_handler["handlerFn"]()
