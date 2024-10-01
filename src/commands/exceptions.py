class UnknownCommandException(Exception):
    def __init__(self, message="You entered an unknown command"):
        super().__init__(message)
