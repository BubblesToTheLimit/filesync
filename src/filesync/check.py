import os
import sys


def generate_source_list(dir_or_file):
    """
    Generate a list of files from a given file or path
    """
    if os.path.isfile(dir_or_file):
        return [dir_or_file]
    elif os.path.isdir(dir_or_file):
        with os.scandir(dir_or_file) as it:
            return [x for x in it if os.path.isfile(x)]
    else:
        print(f"Source Path {dir_or_file} is invalid!")
        sys.exit(1)

def generate_destination_list(given_path):
    """
    Generate a list of files from a given path, including sub-paths.
    """
    result = []

    if not os.path.isdir(given_path):
        print(f"Destination Path {given_path} is invalid!")
        sys.exit(1)
    else:
        for root, dirs, files in os.walk(given_path):
            result += [os.path.relpath(os.path.join(root, file)) for file in files]
        return result
