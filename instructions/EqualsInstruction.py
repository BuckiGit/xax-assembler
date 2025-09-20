from instructions.Instruction import Instruction


class EqualsInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Equals Instruction'

    def __str__(self):
        return f"instructions.EqualsInstruction({self.register_a}, {self.register_b})"