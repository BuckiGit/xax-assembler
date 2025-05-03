import InputReader, Lines, OutputWriter

TEST_SCRIPT:bool = False

if __name__ == '__main__':
    print('Assembling...')
    
    if TEST_SCRIPT:
        file_lines:list[str] = InputReader.read_input_file()
        hex_list:list[str] = []

        for line in file_lines:
            hex_list.append(Lines.Line(line).line_to_hex()[2::])
        
        output:str = OutputWriter.format_output_string(hex_list, True, True)
        OutputWriter.write_output_file(output)
        print(output) # To review output without having to open output.txt

    print('Done!')