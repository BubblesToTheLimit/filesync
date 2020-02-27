import pytest

from filesync import check

from os import walk

example_source = [
    "fileA",
    "fileB",
    "fileC"
]

example_destination = [
    "fileA",
    "folder1/fileB"
]

example_diff = (
    ["fileA", "fileB"],
    ["fileC"]
)

def test_source_list_generation_from_file(mocker):
    """
    If a single file is given as the source, the function still should correctly return a list.
    """
    single_file = example_source[0]
    
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

    assert check.generate_destination_list(test_directory) == example_destination


def test_difference(mocker):
    """
    Given source and destination list, this function should generate 2 lists.
    """
    mocker.patch("check.generate_destination_list", return_value=example_destination)
    mocker.patch("check.generate_source_list", return_value=example_source)

    assert check.difference(example_source, example_destination) == example_diff