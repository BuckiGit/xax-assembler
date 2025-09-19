from enum import Enum

class Error:
    """
    Class to represent and display errors

    Note: Class provides central print definition, use Errors::ErrorTypes class to implement errors

    :param message: Stores the error message
    """
    def __init__(self, message:str=None) -> object:
        """
            :param message: String that stores the error message
        """
        if message == None: raise ValueError("Error message not provided!")
        self.__message:str = message

    def print_error(self, component:str=None) -> None:
        """
            :param component: String that stores the faulty component
        """
        if component == None: raise ValueError("Component not provided!")
        print(f"| {component} - {self.__message}")

class ErrorTypes(Enum):
    """
    Enum to represent errors

    Note: Calling errors: ErrorTypes.<error>.value.print_error(<component>) 
    """
    NOT_ENOUGH_VALUES = Error('Not enough values')
    NO_INSTUCTION = Error('Missing instruction')
    NO_REGISTER = Error('Missing register')
    UNKNOWN_INSTRUCTION = Error('Unknown instruction')
    NON_LOWERCASE_INSTRUCTION = Error('Non-lowercase instruction')
    INVALID_REGISTER_NUMBER = Error('Invalid register number')