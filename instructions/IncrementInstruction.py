from typing import override

from instructions.Instruction import Instruction


class IncrementInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Increment Instruction'

    @override
    def __init__(self, register_a:int, register_b:int):
        super().__init__(register_a, 0)

    def __str__(self):
        return f"instructions.IncrementInstruction({self.register_a})"