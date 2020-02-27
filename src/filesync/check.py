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

def difference(sources, destinations):
    """
    Returns two lists, first a list of files which is included in a destination as a touple, then the files which arent.
    """
    hits = []
    misses = []

    for source in sources:
        hit_found = False
        print("source: " + source)
        for destination in destinations:
            filename = destination.replace(os.path.dirname(destination) + "/", "")
            print(f"comparing {os.path.normpath(source)} =  {os.path.normpath(filename)}")
            if os.path.normpath(source) == os.path.normpath(filename):
                print("found a hit for " + source)
                hits.append((source, destination))
                hit_found = True
                break

        if not hit_found:
            print(f"no match found for {source}")
            misses.append(source)

    print(hits)
    print(misses)

    return (hits, misses)