import InstructionReader, ValueConverter

class Line:
    def __init__(self, line:str):
        self.line:str = line

    def line_to_hex(self) -> str:
        instruction, register1, register2 = self.line.split(';')[0].split(' ')[0:3]

        instruction_bin:str = ValueConverter.hex_to_bin(InstructionReader.get_instruction_set()[instruction])
        register1_bin:str = '0' * (2 - len(ValueConverter.hex_to_bin(register1)[2::])) + ValueConverter.hex_to_bin(register1)[2::]
        register2_bin:str = '0' * (2 - len(ValueConverter.hex_to_bin(register2)[2::])) + ValueConverter.hex_to_bin(register2)[2::]
        
        return ValueConverter.bin_to_hex(instruction_bin + register1_bin + register2_bin)