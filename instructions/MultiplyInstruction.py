from instructions.Instruction import Instruction


class MultiplyInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Multiply Instruction'

    def __str__(self):
        return f"instructions.MultiplyInstruction({self.register_a}, {self.register_b})"