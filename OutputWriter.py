import Paths

def format_output_string(byte_list:list[str], header:bool=None, line_count:bool=None) -> str:
    # TODO: Config file for: Nullbyte, header, file wifth/height
    """
    """
    null_byte = "00"
    list_length = len(byte_list)

    if list_length == 0:
        byte_list = [null_byte] * 16

    elif list_length % 16 != 0:
        byte_list.extend([null_byte] * (16 - (list_length % 16)))

    output:str = ''

    # if None == if False
    if header:
        output = Paths.files_path("header")
    
    for byte in byte_list:
        pass
    
    print(byte_list)
    pass

def write_output_file(content: str) -> None:
    """
        Writes content string to files/output.txt

        Note: String should be preformatted 

        :return: None
    """
    with open(Paths.files_path('output.txt'), 'w') as output_file:
        output_file.write(content)


format_output_string(["00"] * 8)
