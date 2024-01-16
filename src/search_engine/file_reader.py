import os


def make_absolute_path(path: str, levels_up=3) -> str:
    """
    Convert the path to an absolute path with specified levels up.

    Parameters:
    - path (str): The path to be converted.
    - levels_up (int): Number of levels to go up.

    Returns:
    - str: The absolute path.
    """
    # Checking if the path is already absolute
    if os.path.isabs(path):
        return path

    # Calculating the absolute path by going up the specified number of levels
    current_script_path = os.path.abspath(__file__)
    base_path = current_script_path
    for _ in range(levels_up):
        base_path = os.path.dirname(base_path)

    absolute_path = os.path.abspath(os.path.join(base_path, path))
    return absolute_path


def path_does_exist(directory_path: str) -> bool:
    """
    Check if the specified directory exists.

    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - bool: True if the directory exists, False otherwise.
    """
    return os.path.exists(directory_path) and os.path.isdir(directory_path)


def get_directory_contents(directory_path):
    """
    Get a list of dictionaries containing file names and their content in the specified directory.

    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - list: A list of dictionaries with 'file_name' and 'content' keys.
    """
    try:
        # Getting the absolute path
        abs_directory_path = make_absolute_path(directory_path)

        # Checking if the directory exists
        if not path_does_exist(abs_directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        directory_contents = []

        # Iterating through files in the directory
        for filename in os.listdir(abs_directory_path):
            file_path = os.path.join(abs_directory_path, filename)

            # Check if the file is a text file
            if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
                # Read the content of the text file
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    directory_contents.append({'file_name': filename, 'content': content})

        return directory_contents
    except Exception as e:
        print(f"Error: {e}")
        return None
