import sys
from search_engine.engine import Engine
from search_engine.file_reader import path_does_exist, get_directory_contents
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

    file_data = get_directory_contents(directory_path)
    trie_root = build_trie(file_data)

    engine = Engine(trie_root, document_contents=file_data)
    print(f"search-conf> Search engine initialized for files in {directory_path}")

    while True:
        query = input("search> ")

        if query.lower() == ':quit':
            break

        results = engine.search(query=query)
        display_results(results) if results else print("search> No matches found")


def display_results(results):
    for result in results:
        print(f"{result[0]} : {result[1]:.2f}%")


if __name__ == "__main__":
    main()
