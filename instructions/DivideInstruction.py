from instructions.Instruction import Instruction


class DivideInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Divide Instruction'

    def __str__(self):
        return f"instructions.DivideInstruction({self.register_a}, {self.register_b})"