import pytest

from filesync import check

from os import walk

source_example = [
    "fileA",
    "fileB",
    "fileC"
]

destination_example = [
    "fileA",
    "folder1/fileB"
]

def test_source_list_generation_from_file(mocker):
    """
    If a single file is given as the source, the function still should correctly return a list.
    """
    single_file = source_example[0]
    
    mocker.patch("os.path.isfile", return_value=True)
    assert check.generate_source_list(single_file) == [single_file]


def test_destination_list_generation(mocker):
    """
    Given a destination containing directories, the function should correctly return a list.
    """
    test_directory = "."

    mocker.patch("os.walk", return_value=iter([
        (test_directory, ["folder1"], ["fileA"]),
        (test_directory + "/folder1", [], ["fileB"])
    ]))
    mocker.patch("os.path.isdir", return_value=True)

    assert check.generate_destination_list(test_directory) == destination_example