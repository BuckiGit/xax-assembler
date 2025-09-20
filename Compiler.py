import OutputWriter
from InstructionReader import InstructionReader
import Paths
from ConfigManager import ConfigManager
from instructions.Instruction import Instruction

#*************************#
# Options / Customization #
#.........................#

#Test file
"""
add 03
add 00 03; testcomment
nkb GG GG ; deliberately failing line for testing
equ 00 03; testcomment
grt 01 03 ; testcomment2
lss 02 02 ;testcomment3
sub 03 01
add 03 00
nkb GG GG ; deliberately failing line for testing
add 00 ; failing line - not enough values
add ; failing line - not enough values
"""

config:ConfigManager = ConfigManager()

"""
every character after the commentChar is cut out on parsing
lines structured like: "add 00 01 ; <-- this is the commentChar"
"""
commentChar = ';'


instruction_set:dict[str, type[Instruction]] = InstructionReader.get_instruction_set(config)

"""
header taken from comparison file
"""
header = "v3.0 hex words adressed"


"""
behavior lints define how the compiler behaves
they and are active if they're marked as "True"
pattern: "lint" : True / False
"""
behaviourLints = {
    # "trimTwo": True,
    "addRowCounter"       : True,
    "addHeader"           : False,
    "undefinedWriteZeros" : False,
    # "preferFirst"       : True,
    # "preferSecond"      : False,
    "warnNonLowercase"    : True,

}

# comparison file 16 (+ identifier) * 16 00-ff --> len of hexArray = 256

#****************************************************************#
# Compiler Code - Please don't touch unless absolutely necesarry #
#................................................................#
from os import path

errorMessages = [
    "Unknown Instruction",
    "Non-Lowercase Instruction",
    "Missing Value",
    "Unsupportet Value(s)",
]

class LineError:
    def indexError(index: int) -> str:
        return f"Missing value at index {index}"

class Line:
    def __init__(self, line: str, index: int):
        # newline gets removed upon instanciation
        self.line: str = line.removesuffix('\n')
        self.splitLine:list[str] = self.line.split(commentChar)[0].split(' ')
        self.index: int = index

        self.instructionRaw: str | None = None
        self.value1Raw: str | None = None
        self.value2Raw: str | None = None

        self.instruction: str | None = None
        self.value1: str | None = None
        self.value2: str | None = None

        self.hexValue: str|None = None
        self.errors = [] # list(tuple((str, str))))

###########

    def decodeValue(self, valueList: list, index: int, filler: any = None) -> str:
        if filler == None:
            filler = "00"
        
        value:str|None = None
        
        try:
            value: str = valueList[index]
        
        except IndexError:
            self.errors.append(LineError.indexError(index))
            value: str = str(filler)
        
        finally:
            return value


    def decodeLine(self):
        # isolate instruction components (instruction, value1, value2 - Comment cut out)
        # cutLine = self.line.split(commentChar)[0].split(' ')[0:3] # list(str)
        cutLine = self.splitLine
        l = [self.instructionRaw, self.value1Raw, self.value2Raw]
        print(l)

        for index, value in enumerate(l):
            try:
                value = cutLine[index]
                print("v, c:", value + ",", cutLine[index])
            except IndexError:
                print("DBG: IndexError")
                self.errors.append((errorMessages[2], cutLine)) # Missing Value
                # value = "00"
        
            finally:
                print(l)
                if False:
                    print("[DEBUG | TODO] Remove debug-Finally from Line.decodeLine!")
                    print(">"+str(l.instructionRaw)+"<")
                    print(">"+str(l.value1Raw)+"<")
                    print(">"+str(l.value2Raw)+"<")

                if len(cutLine) < 3:
                    return
                print(self.line, value)

###########

    def testInstruction(self) -> None:
        if self.instructionRaw not in instructions:
            self.errors.append((errorMessages[0], self.instructionRaw)) # Unknown Instruction
        else:
            self.instruction = int(instructions[self.instructionRaw], 2)

    def testValue1(self) -> None:
        if int(self.value1Raw) > 3:
            raise ValueError
        else:
            self.value1 = int(self.value1Raw)
        
    def testValue2(self) -> None:
        if int(self.value2Raw) > 3:
            raise ValueError
        else:
            self.value2 = int(self.value2Raw)

    def printErrors(self):
        if len(self.errors) != 0:
            print(f"Errors in line {self.index} ~ \"{self.line}\"")
            for error in self.errors:
                # [/!\] - Warning -+
                # [!!!] - Error   -+-- TODO
                # print(f"| {error[0]}: {error[1]}")
                print(f"| {error}")
            print()

#***********************************************************************#

def to_instruction(line: str) -> Instruction:
    cleaned_line:str = line.removesuffix('\n')
    command_components:list[str] = cleaned_line.split(commentChar)[0].split(' ')
    new_instruction:Instruction = instruction_set[command_components[0]](
        int(command_components[1]),
        int(command_components[2]))
    return new_instruction

if __name__ == "__main__":
    path = path.dirname(__file__)
    lines:list[tuple[int, str]]
    failedLines = [] # list(tuple((int, str)))
    hexByteArray = [] # list(str)
    parsed_instructions:list[Instruction] = []
    config_manager:ConfigManager = ConfigManager()
    instructions = InstructionReader.get_instruction_set(config_manager)


    with open(Paths.files_path('input.txt'), 'r') as inFile:
        lines = list(enumerate(inFile.read().split('\n')))

    for index, line in lines:
        instruction = to_instruction(line)
        parsed_instructions.append(instruction)
        print(instruction)
        continue
        instruction_type = instruction_set[line.split(' ')[0]]
        l = Line(line, index)
        # l.decodeLine()
        print(l.decodeValue(l.splitLine, 0))
        print(l.decodeValue(l.splitLine, 1))
        print(l.decodeValue(l.splitLine, 2))
        # l.testInstruction()
        l.printErrors()
    compiled_instructions:list[list[str]] = [ins.compile() for ins in parsed_instructions]
    compiled_string:str = OutputWriter.format_output_string(compiled_instructions)
    OutputWriter.write_output_file(compiled_string)
    exit()

    # print("Compiling...")

    for lineIdx, line in enumerate(lines):
        while line[0] == ' ':
            line = line[1::]
            
        if line[0] in [commentChar, '\n']:
            continue
        
        line = line.replace('\n', '')
        # line = Line(line.replace('\n', ''))

        print("\n")
        try:
            #   inst r1 r2
            # -> add 02 01
            inst, r1, r2 = line.split(';')[0].split(' ')[0:3] # isolate instruction components
        except Exception as exc:
            print(f"isolating failed ({lineIdx}): {inst, r1, r2} ({exc.args})")

        try:
            r1Double: str = bin(int(r1[::-2]))[2::] # read last two chars of r1 as binary
            r1Double = "0" * (2 - len(r1Double)) + r1Double # confine r1Double to two chars of length (00, 01, 10, 11)
            print(f"r1 passed ({lineIdx}): {r1, r1Double}")
        except Exception as exc:
            print(f"r1 failed ({lineIdx}): {r1, r1Double} ({exc.args})")
            # continue

        try:
            r2Double: str = bin(int(r2[::-2]))[2::] # read last two chars of r2 as binary
            r2Double = "0" * (2 - len(r2Double)) + r2Double # confine r2Double to two chars of length (00, 01, 10, 11)
            print(f"r2 passed ({lineIdx}): {r2, r2Double}")
        except Exception as exc:
            print(f"r2 failed ({lineIdx}): {r2, r2Double} ({exc.args})")
            # continue

        try:
            hexValue = hex(int(("0b" + instructions[inst] + r1Double + r2Double), 2)) # calculate hex value of instruction
            hexValueDouble = "0" * (2 - len(hexValue[2::])) + hexValue[2::] # confine hex value to two chars of length (00-ff)
            print(f"hexV passed ({lineIdx}): {hexValue, hexValueDouble}")
        except Exception as exc:
            print(f"hexV failed ({lineIdx}): {hexValue, hexValueDouble} ({exc.args})")
            # continue

        hexByteArray.append(hexValueDouble)


    if len(failedLines) != 0:
        for lineData in failedLines:
            # TODO: Error output per line
            pass

    if len(hexByteArray < 256):
        # TODO: Warn about overflowing data
        pass
    
    else:
        if len(hexByteArray) < 256:
            hexByteArray.extend((256 - len(hexByteArray)) * ["00"])

        with open(f"{path}\\output.txt") as outFile:
            # TODO
            pass

        # input("Done!\nPress [ENTER] to exit.")
