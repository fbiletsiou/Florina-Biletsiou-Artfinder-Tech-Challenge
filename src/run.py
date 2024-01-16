import sys

from src.search_engine.engine import Engine
from src.search_engine.file_reader import path_does_exist, get_directory_contents
from src.search_engine.trie import build_trie


def main():
    # Checking if command line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python src\\run.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    # Validating the provided directory path
    while not path_does_exist(directory_path=directory_path):
        print(f"search-conf> The directory path '{directory_path}' doesn't seem to exist or is not a directory.")
        directory_path = input("search-conf> Please provide a valid directory path: ")

    # Reading file data from the specified directory
    file_data = get_directory_contents(directory_path)
    # Building Trie from the file data
    trie_root = build_trie(file_data)

    # Initializing the search engine with Trie root and document contents
    engine = Engine(trie_root, document_contents=file_data)
    print(f"search-conf> Search engine initialized for files in {directory_path}")
    print(f"search-conf> {len(file_data)} files read in directory {directory_path}")

    while True:
        # Accepting user input for search query
        query = input("search> ")

        # Exiting the loop if the user enters ':quit'
        if query.lower() == ':quit':
            break

        # Performing the search and displaying results
        results = engine.search(query=query)
        display_results(results) if results else print("search> No matches found")


def display_results(results: list):
    """
    Display search results with file names and corresponding rank scores.

    Parameters:
    - results (list): List of tuples containing file names and their rank scores.

    Returns:
    - None
    """
    for result in results:
        percentage = round(result[1], 2)
        if percentage == int(percentage):
            percentage = int(percentage)
        print(f"{result[0]} : {percentage}%")


if __name__ == "__main__":
    main()
