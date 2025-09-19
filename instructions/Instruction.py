from abc import ABC
from math import floor

from ConfigManager import ConfigManager, Configuration


class Instruction:
    """
        a base class for all instructions
    """

    loaded_class_values: bool = False
    CONFIGURATION_NAME:str
    INSTRUCTION_ID:int
    INSTRUCTION_ASSEMBLER_KEYWORD:str

    def __init__(self, instruction_id:int, register_a:int, register_b:int):
        self.instruction_id:int = instruction_id
        self.register_a:int = register_a
        self.register_b:int = register_b

    def compile(self) -> list[str]:
        return [Instruction.to_hex(self.__class__.INSTRUCTION_ID * 16 + self.register_a * 4 + self.register_b)]

    @classmethod
    def load_class_config_values(cls:type['Instruction'], config_manager:ConfigManager):
        if cls.loaded_class_values:
            return
        configuration:Configuration = config_manager.generate_configuration(cls.CONFIGURATION_NAME)
        cls.INSTRUCTION_ASSEMBLER_KEYWORD = configuration.read_parameter('Assembler Keyword', generate_if_missing=True)
        cls.INSTRUCTION_ID = int(configuration.read_parameter('Instruction Id', generate_if_missing=True))
        cls.loaded_class_values = True

    @staticmethod
    def to_hex(value:int) -> str:
        hex_digits:list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        return hex_digits[floor(value/16)] + hex_digits[value % 16]
