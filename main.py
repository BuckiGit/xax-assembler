import InputReader, Lines, OutputWriter

TEST_SCRIPT:bool = True

if __name__ == '__main__':
    print('Assembling...')
    
    if TEST_SCRIPT:
        file_lines:list[str] = InputReader.read_input_file()
        hex_list:list[str] = []
        failed: bool = False

        for index, line in enumerate(file_lines):
            line = Lines.Line(index, line)
            line.check_errors()

            if len(line.errors) == 0:
                hex_list.append(line.line_to_hex()[2::])
            else: 
                failed = False
        
        if not failed:
            output:str = OutputWriter.format_output_string(hex_list, True, True)
            OutputWriter.write_output_file(output)

        print(output) # To review output without having to open output.txt

    print('Done!')