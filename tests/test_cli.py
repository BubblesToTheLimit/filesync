import pytest

from filesync import cli

def test_failure_if_insufficient_args_given():
    """
    The CLI needs source and destination path. Needs to fail if those are not given.
    """
    insufficient_args = [
        ["--source", "sourcepath/only"],
        ["--destination", "sourcepath/only"]
    ]

    parser = cli.create_parser()
    for args in insufficient_args:
        with raises(SystemExit):
            parser.parse_args(args)