from typing_extensions import override

from instructions.Instruction import Instruction


class InputInstruction(Instruction):
    """

    """

    CONFIGURATION_NAME:str = 'Input Instruction'


    def __init__(self, register_a:int, register_b:int):
        super().__init__(register_a, register_b)

    def __str__(self):
        return f"instructions.InputInstruction({self.register_a}, {self.register_b})"

    @override
    def compile(self) -> list[str]:
        return [Instruction.to_hex(self.__class__.INSTRUCTION_ID*16 + self.register_a*4), Instruction.to_hex(self.register_b)]
