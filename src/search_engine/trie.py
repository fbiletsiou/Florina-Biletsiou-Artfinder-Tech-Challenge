from .tokenizer import tokenize


class TrieNode:
    def __init__(self):
        self.children = {}
        self.documents = set()


def insert_into_trie(root: TrieNode, word: str, document: str):
    """
    Inserts a list of words into the Trie with the associated document.

    Parameters:
    - root (TrieNode): The root of the Trie.
    - words (str): Words to be inserted.
    - document (str): The associated document.

    Returns:
    - None
    """
    node = root
    # Traversing the Trie for each character in the word
    for char in word:
        # Creating a new TrieNode if the character is not in the children
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]  # Moving to the next node in the Trie

    # Adding the document to the set of documents associated with the final node
    node.documents.add(document)


def build_trie(file_data: list):
    """
    Builds a Trie from the given list of file data.

    Parameters:
    - file_data (list): List of dictionaries containing 'file_name' and 'content'.

    Returns:
    - TrieNode: The root of the Trie.
    """
    root = TrieNode()

    # Iterating through each document in the file data
    for document_data in file_data:
        file_name = document_data['file_name']
        content = document_data['content']
        words = tokenize(content)  # Tokenizing the content into words

        # Inserting each word into the Trie with the associated document
        for word in words:
            insert_into_trie(root, word, file_name)

    return root
