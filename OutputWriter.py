import Paths

def format_output_string(byte_list:list[str], header:bool=None, line_count:bool=None) -> str:
    """
        Extends the give byte list to be evenly divisible by 16        
        and formats it into a from LogiSim accepted output

        Note: header=True starts the file with a pre-defined header
              
             line_count=True adds a linecount formatted like: " 00: >Bytes<

        :return: String formatted to be used by OutputWriter.write_output_file()
    """
    null_byte:str = "00"
    header_string:str = "v3.0 hex words adressed"
    list_length:int = len(byte_list)

    if list_length == 0:
        byte_list = [null_byte] * 16

    elif list_length % 16 != 0:
        byte_list.extend([null_byte] * (16 - (list_length % 16)))

    output:str = ''

    # if None == if False
    if header:
        output += f"{header_string}\n"
    
    for byte_index, byte in enumerate(byte_list):
        # if None == if False
        if line_count and byte_index % 16 == 0:
            output += f'{"0" * (2 - (len(hex(byte_index)[2::]))) + hex(byte_index)[2::]}: '

        output += f'{byte} '

        if (byte_index + 1) % 16 == 0 and byte_index != 0: 
            output += '\n'
        

    return output

def write_output_file(content: str) -> None:
    """
        Writes content string to files/output.txt

        Note: String should be preformatted 

        :return: None
    """
    with open(Paths.files_path('output.txt'), 'w') as output_file:
        output_file.write(content)