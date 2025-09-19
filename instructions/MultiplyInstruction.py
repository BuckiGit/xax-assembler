from instructions.Instruction import Instruction


class MultiplyInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Multiply Instruction'


    def __init__(self, register_a:int, register_b:int):
        super().__init__(MultiplyInstruction.INSTRUCTION_ID, register_a, register_b)