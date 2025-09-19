import InstructionReader, ValueConverter, Errors

class Line:
    """
    Class to represent a program's line, consisting of a instruction and two register values

    Class is used to convert lines to hexadecimal values, handle error checks, ...

    :param index: Stores the line's index
    :param line: Stores the given line string

    :param errors: Stores errors if they occure

    line_to_hex(): returns the line's line formatted to a hexadecimal string
    """
    def __init__(self, index: int, line:str) -> object:
        """
            :param line: the line of code the object will represent
            
            :returns: Line object
        """
        self.index:int = index
        self.line:str = line
        self.errors:list[tuple[Errors.ErrorTypes, str]] = []

    def line_to_hex(self) -> str:
        """
            Formats line's instruction + register 1 + register 2

            Note: Format: hex( 0000_00_00 ) ; hex( < instruction > < register 1 > < register 2 > )

            :returns: Hexadecimal value (starting with "0x")
        """
        instruction, register1, register2 = self.line.split(';')[0].split(' ')[0:3]

        instruction_bin:str = ValueConverter.hex_to_bin(InstructionReader.get_instruction_set()[instruction])
        register1_bin:str = '0' * (2 - len(ValueConverter.hex_to_bin(register1)[2::])) + ValueConverter.hex_to_bin(register1)[2::]
        register2_bin:str = '0' * (2 - len(ValueConverter.hex_to_bin(register2)[2::])) + ValueConverter.hex_to_bin(register2)[2::]
        
        converted:str = ValueConverter.bin_to_hex(instruction_bin + register1_bin + register2_bin)
        # assumes that the hex code never excedes 'ff'
        return converted[:2] + '0' + converted[2::] if len(converted) == 3 else converted
    
    def check_errors(self) -> None:
        """
            Checks the line for errors and stores them to the objects error list

            :returns: None
        """
        instruction, register1, register2 = None, None, None
        input_line = self.line.split(';')[0].split(' ')[0:3]

        if len(input_line) < 3:
            self.errors.append((Errors.ErrorTypes.NOT_ENOUGH_VALUES, ''))
        
        try:
            instruction = input_line[0]
        except:
            self.errors.append((Errors.ErrorTypes.NO_INSTUCTION, ''))
        
        try:
            register1 = input_line[1]
        except:
            self.errors.append((Errors.ErrorTypes.NO_REGISTER, f"{register1}"))
        
        try:
            register2 = input_line[2] 
        except:
            self.errors.append((Errors.ErrorTypes.NO_REGISTER, f"{register2}"))

        try:
            if not instruction in InstructionReader.get_instruction_set().keys():
                self.errors.append((Errors.ErrorTypes.UNKNOWN_INSTRUCTION, f"{instruction}"))
        except:
            self.errors.append((Errors.ErrorTypes.UNKNOWN_INSTRUCTION, f"{instruction}"))
        
        try: 
            if not instruction == instruction.lower():
                self.errors.append((Errors.ErrorTypes.NON_LOWERCASE_INSTRUCTION, f"{instruction}"))
        except:
            self.errors.append((Errors.ErrorTypes.NON_LOWERCASE_INSTRUCTION, f"{instruction}"))

        try:
            if not (0 <= int(register1, 16) <= 3):
                self.errors.append((Errors.ErrorTypes.INVALID_REGISTER_NUMBER, f"{register1}"))
        except: 
            self.errors.append((Errors.ErrorTypes.INVALID_REGISTER_NUMBER, f"{register1}"))

        try:
            if not (0 <= int(register2, 16) <= 3):
                self.errors.append((Errors.ErrorTypes.INVALID_REGISTER_NUMBER, f"{register2}"))
        except: 
            self.errors.append((Errors.ErrorTypes.INVALID_REGISTER_NUMBER, f"{register2}"))

        if len(self.errors) != 0:
            # Differentiate errors with "prefixes?" (e.g.: "| [!!!] <Token> <Message>!")
            # [!!!] for genuine, codebreaking errors (red)
            # [/!\\] for oversights, such as "too many arguments" (useless arguments could be ignored) (yellow)
            print(f"\nLine {self.index}: {self.line}")
            for error_data in self.errors:
                error_data[0].value.print_error(error_data[1])