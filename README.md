# Command Line Text Search Engine
## Florina Biletsiou - Artfinder Tech Challenge

## Description

This is a simple command line driven text search engine implemented in Python. The program reads all text files in a specified directory, builds an in-memory representation of the files and their contents, and provides an interactive command prompt for text searches.

## Usage

```bash
python <filename> <pathToDirectoryContainingTextFiles>
```

Example:

```bash
python simplesearch.py /foo/bar
```

## Features

- Reads all text files in the specified directory.
- Builds an efficient in-memory representation for text search.
- Supports interactive searches with a command prompt.
- Provides ranking scores for search results.
- Flexible ranking formula (details in implementation).

## Example Session

```bash
$ python simplesearch.py /foo/bar
14 files read in directory /foo/bar
search>
search> to be or not to be
filename1: 100%
filename2: 95%
search>
search> cats
no matches found
search> :quit
$
```

## Ranking

- 100% if a file contains all the words.
- 0% if it contains none of the words.
- Between 0 and 100 if it contains only some of the words (ranking formula customizable).

## Implementation Details

### Word Definition

- Words are defined based on whitespace separation.

### Matching Words

- Two words are considered equal (and matching) if they are identical.

### Data Structure Design

- In-memory representation optimized for efficient search (details in the code).

### Ranking Score

- A basic ranking score is implemented, and it can be customized as needed.

### Testability

- The program is designed to be testable.
- Unit tests and integration tests can be added and executed.

## How to Run Tests

To run tests, use the following command:

```bash
python test_search_engine.py
```

## Author

[Florina Biletsiou](https://florinabiletsiou.com/)  
Connect with me on [LinkedIn](https://www.linkedin.com/in/florina-biletsiou/)
