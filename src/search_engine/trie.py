from .tokenizer import tokenize


class TrieNode:
    def __init__(self):
        self.children = {}
        self.documents = set()


def insert_into_trie(root, word, document):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.documents.add(document)



def build_trie(file_data: list):
    root = TrieNode()

    for document_data in file_data:
        file_name = document_data['file_name']
        content = document_data['content']
        words = tokenize(content)

        for word in words:
            insert_into_trie(root, word, file_name)

    return root
