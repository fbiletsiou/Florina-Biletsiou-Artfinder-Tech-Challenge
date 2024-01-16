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
python src/run.py demo_files
```

## Features

- **File Reading**: The search engine reads all text files within a specified directory, ensuring comprehensive coverage of available content. 
- **In-Memory Representation**: An efficient in-memory representation is built for the text content, optimizing the search process. This involves utilizing a Trie data structure to facilitate quick and effective word-based searches. 
- **Interactive Search**: The search engine offers an interactive command-line prompt, allowing users to input search queries and receive dynamic results. 
- **Ranking Scores**: Search results are accompanied by ranking scores, providing users with an indication of the relevance of each file to the given query. 


## Example Session

```bash
$ python src/run.py demo_files
search-conf> Search engine initialized for files in demo_files
search-conf> 20 files read in directory demo_files
search>Musée d\'Orsay, Paris
The Starry Night Over the Rhone.txt : 100%
Whistlers Mother.txt : 100%
Water Lilies.txt : 66.67%
Mona Lisa.txt : 33.33%
search> Cat
search> No matches found
search> 
search> :quit
$
```

## Ranking
The ranking system provides a score between 0 and 100 for each file based on the search query. The rules for scoring are as follows:

### Perfect Match (100%)
- Scenario: If a document contains every word from the search query. 
- Rank Score: 100.0% 
- Interpretation: A perfect match indicates that the document includes all the words specified in the search query.

### No Match (0%)
- Scenario: If there are no common words between the document and the search query.
- Rank Score: 0.0%
- Interpretation: A 0.0% score signifies no overlap between the document's content and the words in the search query.

### Partial Match (0-100%)
- Scenario: The document contains some, but not all, of the words from the search query.
- Rank Score: Varies between 0 and 100%, reflecting the ratio of common words.
- Calculation: The score is determined by the ratio of common words to the total distinct words in the search query.
- Example: If the document includes half of the words in the search query, the score is 50.0%.

The ranking formula is designed to provide a nuanced evaluation of the degree to which a file matches the given search query.


## Implementation Details

### Word Definition

The search engine employs a tokenization process to break down the content into individual words, facilitating efficient indexing and search capabilities. The tokenization process involves several key steps:

#### Tokenization Steps:
1. **Whitespace Separation**:
   - The content is split into individual words based on whitespace. 
   - Example: The sentence `Search engine tokenization` is split into `["Search", "engine", "tokenization"]`.
2. **Punctuation Handling**:
   - Punctuation marks are removed from each word, ensuring accurate and clean tokenization.
   - Example: The word `"example!"` becomes `"example"` after removing the exclamation mark.
3. **Lower-casing**:
   - All words are converted to lowercase to ensure case-insensitive search capabilities.
   - Example: The word `"Search"` is converted to `"search"`.

#### Tokenization Benefits:
- **Efficient Indexing**:<br>
  Tokenization allows for the creation of an efficient in-memory representation of files, enhancing search performance.
- **Case-Insensitive Searching**:<br>
  Lower-casing ensures that search queries are case-insensitive, providing a seamless and user-friendly search experience.

### Matching Words
The core functionality of the search engine revolves around identifying and ranking documents based on the presence of matching words between user queries and document contents. This section provides detailed insights into the process of matching words and how the search engine determines the relevance of documents to specific search queries.

#### Matching Words Process:
1. **Tokenization**:
   - Content and search queries undergo tokenization, breaking them into individual words.
   - The tokenization process ensures a standardized representation for efficient matching.
2. **Intersection Calculation**:
   - The engine calculates the intersection of words between the search query and document content.
   - This intersection represents the common words shared between the query and the document.
3. **Ranking Score**:
   - A ranking score is assigned to each document based on the intersection of words.
   - The scoring system reflects the degree of match between the query and document, ranging from 0% to 100%.

#### Implementation Details:
`calculate_rank_score` Method:<br>
This method in the Engine class plays a crucial role in calculating the rank score for a document based on the query.
It provides the foundation for the ranking system, allowing users to define the importance of matching words in the scoring.

### Trie Data Structure Design

The search engine employs a Trie data structure to create an efficient and optimized in-memory representation for text search. 
<br>The Trie design facilitates quick and effective search capabilities, enhancing the performance of the search engine. Below are the key components and design considerations:

#### Components of the Trie:

1. **Trie Node:**
   - The fundamental building block of the Trie is a node, represented by the `TrieNode` class.
   - Each node contains two main attributes: `children` and `documents`.
     - `children`: A dictionary that maps characters to child nodes, representing the branching structure of the Trie.
     - `documents`: A set that stores the associated documents at a particular node.

2. **Insertion Process:**
   - The `insert_into_trie` function is responsible for inserting words into the Trie.
   - For each character in a word, a corresponding node is created if it does not already exist, forming a branching structure.
   - The `documents` set at the final node of a word stores the names of documents containing that word.

3. **Building the Trie:**
   - The `build_trie` function constructs the Trie from a given list of file data.
   - For each document in the data, its content is tokenized into words, and each word is inserted into the Trie.

#### Trie Benefits:

- **Efficient Search:**
  - The Trie data structure allows for efficient prefix-based searches, making it well-suited for word-based queries.
  - Search operations have a time complexity proportional to the length of the search query.

- **Memory Efficiency:**
  - The Trie optimally uses memory by sharing common prefixes among words, reducing redundancy in storage.

- **Dynamic Structure:**
  - The Trie dynamically adapts to changes in the dataset, making it suitable for dynamic content updates and additions.

#### Trie in the Search Engine:

- **Tokenization and Indexing:**
  - During the tokenization process, words extracted from document content are efficiently indexed into the Trie.
  - This indexing process enables quick and precise search capabilities by traversing the Trie based on query words.

- **Support for Partial Matches:**
  - The Trie supports partial matches, allowing for partial queries to efficiently retrieve relevant documents.

- **Scalability:**
  - The Trie's dynamic structure and efficient search mechanisms contribute to the scalability of the search engine.

By leveraging the Trie data structure, the search engine achieves a balance between search efficiency, memory optimization, and support for dynamic content, providing users with a powerful and responsive search experience.
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
