from instructions.Instruction import Instruction


class AddInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Add Instruction'

    def __str__(self):
        return f"instructions.AddInstruction({self.register_a}, {self.register_b})"