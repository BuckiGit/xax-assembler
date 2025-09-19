from instructions.Instruction import Instruction


class AddInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Add Instruction'


    def __init__(self, register_a:int, register_b:int):
        super().__init__(AddInstruction.INSTRUCTION_ID, register_a, register_b)

    def __str__(self):
        return f"instructions.AddInstruction({self.register_a}, {self.register_b})"