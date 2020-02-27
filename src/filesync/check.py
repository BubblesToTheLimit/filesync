from os import path, scandir
import sys

def generate_source_list(path_or_file):
    """
    Generate a list of files from a given file or path
    """
    if path.isfile(path_or_file):
        return [path_or_file]
    elif path.isdir(path_or_file):
        with scandir(path_or_file) as it:
            return [x for x in it if path.isfile(x)]
    else:
        print(f"Source Path {path_or_file} is invalid!")
        sys.exit(1)

