from instructions.Instruction import Instruction


class JumpInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Jump Instruction'

    def __str__(self):
        return f"instructions.JumpInstruction({self.register_a})"