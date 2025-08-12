class Variable:
    """

    """

    def __init__(self, instruction_pattern: str, instruction_byte: int):
        self.instruction_pattern: str = instruction_pattern
        self.instruction_byte: int = instruction_byte;

    def interpret_line(self):
        pass

    def compile_line(self):
        pass