from os import path
from filesync import check

source_example = [
    "fileA",
    "fileB",
    "fileC"
]

destination_example = [
    "fileA"
    "folder1/fileB"
]

def test_source_list_generation_from_file(mocker):
    """
    If a single file is given as the source, the function still should correctly return a list.
    """
    single_file = source_example[0]
    
    mocker.mock("os.path.isfile", return_values=True)
    assert check.generate_source_list[single_file] == [single_file]


def test_destination_list_generation(mocker):
    """
    Given a destination containing directories, the function should correctly return a list.
    """
    test_directory = "somedir"

    mocker.mock("os.fwalk", return_values=[
        (test_directory, ["folder1"], ["fileA"], 1),
        (test_directory + "/folder1", [], ["fileB"], 1)
    ])

    assert check.generate_destination_list(test_directory) == destination_example