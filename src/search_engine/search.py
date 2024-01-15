
from .trie import TrieNode
from .tokenizer import tokenize


def search_and_rank(query: str, trie_root: TrieNode) -> list:
    """
    Search for documents in the Trie based on the given query and rank the results.

    Parameters:
    - query (str): The search query.
    - trie_root (TrieNode): The root of the Trie.

    Returns:
    - list: A list of tuples containing filename and rank score.
    """
    # Tokenize the query
    query_tokens = tokenize(query)

    # Perform search in the Trie
    matching_documents = get_matching_documents(query_tokens, trie_root)

    # Rank the results
   #  ranked_results = rank_search_results(query_tokens, matching_documents)

    # return ranked_results
    return matching_documents


def get_matching_documents(query_tokens: list, trie_root: TrieNode) -> set:
    matching_documents = set()
    node = trie_root

    for word in query_tokens:
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                break
        else:
            # The inner loop completed without breaking, meaning the entire word was found
            matching_documents.update(node.documents)
            node = trie_root  # Reset to the root for the next word

    return matching_documents


def rank_search_results(query_tokens: list, matching_documents: set) -> list:
    # Implement a ranking algorithm based on the query and matching documents
    pass
