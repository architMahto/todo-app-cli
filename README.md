# todo-app-cli

This app is a CRUD cli tool to manage todos. The todos are stored and managed in a local file.

## Preqrequisites

### Programs, Databases, or Runtime Environments

* `Poetry`

### Environment Variables

N/A

## How to Run

### Application

1. `poetry run python main.py`

### Tests, Linting and Formatting

#### Without Coverage

1. `poetry run pytest -v ./tests`

#### With Coverage

1. `poetry run pytest -v --cov=src --cov-report term ./tests`

##### With HTML

1. `poetry run pytest -v --cov=src --cov-report html ./tests`

#### Linting

1. `poetry run pylint src`

#### Formatting

1. `poetry run python -m black src`
