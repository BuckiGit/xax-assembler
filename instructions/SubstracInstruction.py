from instructions.Instruction import Instruction


class SubtractInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Subtract Instruction'

    def __str__(self):
        return f"instructions.SubtractInstruction({self.register_a}, {self.register_b})"