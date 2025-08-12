from abc import ABC, abstractmethod


class Instruction(ABC):
    """

    """
    def __init__(self, instruction_pattern:str, instruction_byte:int):
        self.instruction_pattern:str = instruction_pattern
        self.instruction_byte:int = instruction_byte

    @abstractmethod
    def compile_line(self):
        pass