from typing import override

from instructions.Instruction import Instruction


class PassInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Pass Instruction'

    @override
    def __init__(self, register_a:int, register_b:int):
        super().__init__(0, 0)

    def __str__(self):
        return f"instructions.PassInstruction({self.register_a}, {self.register_b})"