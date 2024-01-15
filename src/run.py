import sys
from search_engine.engine import SearchEngine
from search_engine.search import search_and_rank
from search_engine.file_reader import path_does_exist, get_directory_contents
from src.search_engine.trie import build_trie


def initialize_search_engine(directory_path):
    return 1


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

    # Build Trie based on file data
    trie_root = build_trie(get_directory_contents(directory_path))

    # Initialize the search engine
    search_engine = initialize_search_engine(directory_path)

    if search_engine is not None:
        print(f"search-conf> Search engine initialized for files in {directory_path}")

        while True:
            query = input("search> ")

            if query.lower() == ':quit':
                print("Exiting the search engine.")
                break

            print(f'[DEBUG] your input: {query}')
            results = search_and_rank(query=query, trie_root=trie_root)
            print(f'[DEBUG] results: {results}')

            """
            # Perform the search
            results = search_engine.search(query)

            # Display search results
            if results:
                for filename, score in results:
                    print(f"{filename} : {score}%")
            else:
                print("No matches found")            
            """


if __name__ == "__main__":
    main()
