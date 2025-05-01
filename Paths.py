from os import path

main_path_string:str = path.dirname(__file__)

def main_path(relative_path:str) -> str:
    """
        Resolves target path from relative path
        
        :return: mainpath joined with relative path
    """
    return main_path_string + ('/' if not relative_path.startswith('/') else '') + relative_path
    
def files_path(relative_path:str) -> str:
    """
        Resolves target path from relative path
    
        :return: mainpath/files joined with relative path
    """
    return main_path('/files' + ('/' if not relative_path.startswith('/') else '') + relative_path)