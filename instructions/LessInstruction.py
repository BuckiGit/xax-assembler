from instructions.Instruction import Instruction


class LessInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Less Instruction'

    def __str__(self):
        return f"instructions.EqualsInstruction({self.register_a}, {self.register_b})"