"""This module exports handler functions for the tui"""

from src.services.todos import get_todos, add_todo, edit_todo, complete_todo
from src.validators.todos import validate_select_todo


def display_todos(todos):
    """This method is used to print the todos in a user friendly display"""
    for idx, item in enumerate(todos):
        print(f"{idx + 1}. {item.strip('\n')}")


def handle_get_todos():
    display_todos(get_todos())


def handle_add_todo(new_todo):
    add_todo(new_todo)


@validate_select_todo
def handle_edit_todo(selected_todo):
    print("Here are current todos:")
    display_todos(get_todos())

    new_todo = input("Enter new todo: ")
    edit_todo(selected_todo, new_todo)

    print("Here are new todos:")
    display_todos(get_todos())


@validate_select_todo
def handle_complete_todo(selected_todo):
    todos = get_todos()
    complete_todo(selected_todo)

    completed_todo = todos[selected_todo].strip("\n")

    print(f"{completed_todo} was completed.")
