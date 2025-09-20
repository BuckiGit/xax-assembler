from instructions.Instruction import Instruction


class CopyInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Copy Instruction'

    def __str__(self):
        return f"instructions.CopyInstruction({self.register_a}, {self.register_b})"