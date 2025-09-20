from instructions.Instruction import Instruction


class PassInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Pass Instruction'

    def __str__(self):
        return f"instructions.PassInstruction({self.register_a}, {self.register_b})"