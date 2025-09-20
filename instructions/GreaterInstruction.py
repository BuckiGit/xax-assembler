from instructions.Instruction import Instruction


class GreaterInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Greater Instruction'

    def __str__(self):
        return f"instructions.GreaterInstruction({self.register_a}, {self.register_b})"