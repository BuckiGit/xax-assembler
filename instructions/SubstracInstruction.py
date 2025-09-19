from instructions.Instruction import Instruction


class SubtractInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Subtract Instruction'


    def __init__(self, register_a:int, register_b:int):
        super().__init__(SubtractInstruction.INSTRUCTION_ID, register_a, register_b)

    def __str__(self):
        return f"instructions.SubtractInstruction({self.register_a}, {self.register_b})"