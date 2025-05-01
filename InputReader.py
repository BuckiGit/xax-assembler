import Paths

def read_input_file() -> list[str]:
    with open(Paths.files_path('input.txt'), 'r') as input_file:
        lines:list[str] = []
        
        for line in input_file:
            lines.append(line.replace('\n', ''))

    return lines