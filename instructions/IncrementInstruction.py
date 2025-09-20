from instructions.Instruction import Instruction


class IncrementInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Increment Instruction'

    def __str__(self):
        return f"instructions.IncrementInstruction({self.register_a})"