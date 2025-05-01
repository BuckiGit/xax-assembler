import Paths

def get_instruction_set() -> dict:
    instructions = {}
    
    with open(Paths.files_path('instructions.txt'), 'r') as instruction_file:
        for line in instruction_file:
            instruction, value = line.replace('\n', '').split(':')
            instructions.update({instruction : value})

    return instructions