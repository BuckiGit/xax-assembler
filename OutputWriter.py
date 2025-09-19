from math import floor

import Paths

def format_output_string(compiled_instructions:list[str], header:bool=False, line_count:bool=False) -> str:
    # TODO: Config file for: Nullbyte, header, file wifth/height
    """
    """
    null_byte = "00"
    output:str = 'v3.0 hex words addressed'
    n:int = 0
    line_count:int=0
    for i in range(128):
        if i<len(compiled_instructions):
            for byte in compiled_instructions[i]:
                if n >= 128:
                    break
                if n%16==0:
                    output += '\n'
                    output += __to_hex(line_count*16)
                    line_count+=1
                    output += ": "
                output+=byte
                output += ' '
                n+=1
        else:
            if n >= 128:
                break
            if n%16==0:
                output += '\n'
                output += __to_hex(line_count*16)
                line_count+=1
                output += ": "
            output+=null_byte
            output += ' '
            n+=1
    return output

def write_output_file(content: str) -> None:
    """
        Writes content string to files/output.txt

        Note: String should be preformatted 

        :return: None
    """
    with open(Paths.files_path('output.txt'), 'w') as output_file:
        output_file.write(content)


def __to_hex(value:int) -> str:
    hex_digits: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    return hex_digits[floor(value / 16)] + hex_digits[value % 16]