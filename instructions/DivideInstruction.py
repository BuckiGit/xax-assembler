from instructions.Instruction import Instruction


class DivideInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Divide Instruction'


    def __init__(self, register_a:int, register_b:int):
        super().__init__(DivideInstruction.INSTRUCTION_ID, register_a, register_b)