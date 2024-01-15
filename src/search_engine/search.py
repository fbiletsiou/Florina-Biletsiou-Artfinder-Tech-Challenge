
from .trie import TrieNode
from .tokenizer import tokenize


def search_and_rank(query: str, trie_root: TrieNode, file_contents) -> list:
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
    ranked_results = rank_search_results(query_tokens, matching_documents, document_contents=file_contents)

    return ranked_results


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


def rank_search_results(query_tokens: list, matching_documents: set, document_contents: dict) -> list:
    ranked_results = []

    for document_data in document_contents:
        file_name = document_data['file_name']
        content = document_data['content']

        if file_name in matching_documents:
            score = calculate_rank_score(query_tokens, content)
            ranked_results.append((file_name, score))

    # Sort results by score in descending order
    ranked_results.sort(key=lambda x: x[1], reverse=True)

    return ranked_results[:10]  # Return top 10 results


def calculate_rank_score(query_tokens: list, document: str) -> float:
    document_words = tokenize(document)
    intersection = set(query_tokens) & set(document_words)

    if not intersection:
        return 0.0

    if set(query_tokens) == intersection:
        return 100.0

    return len(intersection) / len(set(query_tokens)) * 100.0