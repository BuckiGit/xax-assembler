import Paths

def write_output_file(content: str) -> None:
    """
        Writes content string to files/output.txt

        Note: String should be preformatted 

        :return: None
    """
    with open(Paths.files_path('output.txt'), 'w') as output_file:
        output_file.write(content)