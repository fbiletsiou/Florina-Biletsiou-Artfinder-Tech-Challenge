import os
import shutil
import tempfile
import pytest

from src.search_engine.file_reader import make_absolute_path, path_does_exist, get_directory_contents


@pytest.fixture
def temp_directory():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir

    # Clean up the directory, ensuring it is empty
    try:
        shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Error cleaning up temp directory: {e}")


@pytest.fixture
def temp_directory_with_file(temp_directory):
    # Create a temporary directory with a file
    file_path = os.path.join(temp_directory, 'example.txt')
    with open(file_path, 'w') as file:
        file.write('Sample content')
    return temp_directory


def test_make_absolute_path(temp_directory):
    relative_path = "example.txt"
    script_path = os.path.abspath(__file__)
    # Going two levels up from the script's location
    script_parent = os.path.dirname(os.path.dirname(script_path))
    absolute_path = make_absolute_path(relative_path)

    assert os.path.isabs(absolute_path)
    # Constructing the expected absolute path
    expected_path = os.path.join(script_parent, relative_path)
    assert absolute_path == expected_path


def test_path_does_exist(temp_directory):
    existing_directory = temp_directory
    non_existing_directory = os.path.join(temp_directory, "non_existing_dir")

    assert path_does_exist(existing_directory)
    assert not path_does_exist(non_existing_directory)


def test_path_does_exist_existing_directory(temp_directory_with_file):
    assert path_does_exist(temp_directory_with_file)


def test_path_does_exist_nonexistent_directory(temp_directory):
    non_existent_directory = os.path.join(temp_directory, 'nonexistent')
    assert not path_does_exist(non_existent_directory)


def test_get_directory_contents_valid_directory(temp_directory_with_file):
    contents = get_directory_contents(temp_directory_with_file)
    assert contents == [{'file_name': 'example.txt', 'content': 'Sample content'}]


def test_get_directory_contents_with_subdirectories(temp_directory):
    # Create a subdirectory with a file
    subdirectory_path = os.path.join(temp_directory, 'subdirectory')
    os.makedirs(subdirectory_path)
    file_path = os.path.join(subdirectory_path, 'subfile.txt')
    with open(file_path, 'w') as file:
        file.write('Subdirectory content')

    contents = get_directory_contents(temp_directory)
    assert contents ==[]


def test_get_directory_contents(temp_directory):
    file_content = "This is a test file."
    file_name = "test.txt"
    file_path = os.path.join(temp_directory, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(file_content)

    result = get_directory_contents(temp_directory)
    assert len(result) == 1
    assert result[0]["file_name"] == file_name
    assert result[0]["content"] == file_content
