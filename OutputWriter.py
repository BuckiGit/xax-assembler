import Paths

def write_output_file(content: str) -> None:
    with open(Paths.files_path('output.txt'), 'w') as output_file:
        output_file.write(content)