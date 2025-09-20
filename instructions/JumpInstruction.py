from typing import override

from instructions.Instruction import Instruction


class JumpInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Jump Instruction'

    @override
    def __init__(self, register_a:int, register_b:int):
        super().__init__(register_a, 0)

    def __str__(self):
        return f"instructions.JumpInstruction({self.register_a})"