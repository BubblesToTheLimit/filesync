from argparse import ArgumentParser

def create_parser():
    parser = ArgumentParser("filesync",
        description="Check that files from source directories are available in destination directory."
    )
    parser.add_argument("--source", "-s", help="Source file or directory", required=True)
    parser.add_argument("--destination", "-d", help="Destination directory", required=True)

    return parser