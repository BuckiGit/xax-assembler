from ConfigManager import ConfigManager
from instructions import LessInstruction
from instructions.GreaterInstruction import GreaterInstruction

from instructions.Instruction import Instruction
from instructions.CopyInstruction import CopyInstruction
from instructions.AddInstruction import AddInstruction
from instructions.DivideInstruction import DivideInstruction
from instructions.MultiplyInstruction import MultiplyInstruction
from instructions.PassInIstruction import PassInstruction
from instructions.SubstracInstruction import SubtractInstruction
from instructions.EqualsInstruction import EqualsInstruction
from instructions.InputInstruction import InputInstruction
from instructions.JumpInstruction import JumpInstruction
from instructions.LessInstruction import LessInstruction
from instructions.IncrementInstruction import IncrementInstruction

class InstructionReader:
    """
        loads all instructions from a config file
    """

    __instruction_class_list:list[type[Instruction]] = [
        PassInstruction,
        AddInstruction,
        SubtractInstruction,
        IncrementInstruction,
        EqualsInstruction,
        GreaterInstruction,
        LessInstruction,
        MultiplyInstruction,
        DivideInstruction,
        CopyInstruction,
        InputInstruction,
        JumpInstruction
    ]
    __instruction_set:dict[str, type[Instruction]] = {}

    __loaded:bool = False

    @staticmethod
    def load(config_manager:ConfigManager|None) -> None:
        if InstructionReader.__loaded:
            return
        if config_manager is None:
            return
        for instruction_class in InstructionReader.__instruction_class_list:
            instruction_class.load_class_config_values(config_manager)
            InstructionReader.__instruction_set.update({instruction_class.INSTRUCTION_ASSEMBLER_KEYWORD: instruction_class})
        InstructionReader.__loaded = True



    @staticmethod
    def get_instruction_set(config_manager:ConfigManager|None=None) -> dict[str, type[Instruction]]:
        """
            Reads files/instructions.txt

            :return: instructions / hex-values as dict[str, str]

        """
        if not InstructionReader.__loaded:
            InstructionReader.load(config_manager)
        return InstructionReader.__instruction_set

    @staticmethod
    def get_instruction_classes(config_manager:ConfigManager|None=None) -> list[type[Instruction]]:
        """
            Reads files/instructions.txt

            :return: instructions / hex-values as dict[str, str]

        """
        if not InstructionReader.__loaded:
            InstructionReader.load(config_manager)
        return InstructionReader.__instruction_class_list