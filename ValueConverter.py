def bin_to_hex(value:str) -> str:
    """
        Converts given value to hexadecimal

        Note: A prefix ('0b') will get added to values not starting with it 

        :param str value: Expects value to be a binary string e.g. "0b1100"

        :return: Given value as hexadecimal string
    """
    value = ('' if value.startswith('0b') else '0b') + value
    return hex(int(value, 2))

def hex_to_bin(value:str) -> str:
    """
        Converts given value to binary

        Note: A prefix ('0x') will get added to values not starting with it 

        :param str value: Expects value to be a hexadecimal string e.g. "0xaa00"

        :return: Given value as binary string
    """
    value = ('' if value.startswith('0x') else '0x') + value
    return bin(int(value, 16))