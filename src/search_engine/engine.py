from .trie import TrieNode
from .tokenizer import tokenize


class Engine:
    def __init__(self, trie_root: TrieNode, document_contents: list):
        """
        Initialize the search engine.

        Parameters:
        - trie_root (TrieNode): The root of the Trie.
        - document_contents (list): List of dictionaries containing 'file_name' and 'content'.
        """
        self.trie_root = trie_root
        self.document_contents = document_contents

    @staticmethod
    def calculate_rank_score(query_tokens: list, document: str) -> float:
        """
        Calculate the rank score for a document based on the query.

        Parameters:
        - query_tokens (list): List of tokens from the query.
        - document (str): Content of the document.

        Returns:
        - float: The rank score.
        """
        try:
            document_words = tokenize(document)
            intersection = set(query_tokens) & set(document_words)

            if not intersection:
                return 0.0

            if set(query_tokens) == intersection:
                return 100.0

            return len(intersection) / len(set(query_tokens)) * 100.0
        except Exception as e:
            print(f"Error calculating rank score: {e}")
            return 0.0

    def get_matching_documents(self, query: str) -> set:
        """
        Get a set of documents that match the query.

        Parameters:
        - query (str): The search query.

        Returns:
        - set: Set of matching documents.
        """
        try:
            # Tokenizing the query
            query_tokens = tokenize(query)

            matching_documents = set()
            node = self.trie_root

            for word in query_tokens:
                # Traversing the Trie character by character for the current word
                for char in word:
                    # Checking if the character is present in the current node's children
                    if char in node.children:
                        # Moving to the next node in the Trie for the current character
                        node = node.children[char]
                    else:
                        # Breaking the loop if the character is not found in the Trie
                        break
                else:
                    # The inner loop completed without breaking, meaning the entire word was found
                    matching_documents.update(node.documents)
                    node = self.trie_root  # Reset to the root for the next word

            return matching_documents
        except Exception as e:
            print(f"Error getting matching documents: {e}")
            return set()

    def rank_search_results(self, query: str, matching_documents: set) -> list:
        """
        Rank the search results based on the query.

        Parameters:
        - query (str): The search query.
        - matching_documents (set): Set of matching documents.

        Returns:
        - list: List of ranked search results.
        """
        try:
            # Tokenizing the query
            query_tokens = tokenize(query)

            ranked_results = []

            for document_data in self.document_contents:
                file_name = document_data['file_name']
                content = document_data['content']

                if file_name in matching_documents:
                    score = self.calculate_rank_score(query_tokens, content)
                    ranked_results.append((file_name, score))

            # Sorting results by score in descending order
            ranked_results.sort(key=lambda x: x[1], reverse=True)

            return ranked_results[:10]  # Returning top 10 results
        except Exception as e:
            print(f"Error ranking search results: {e}")
            return []

    def search(self, query: str) -> list:
        """
        Perform a search based on the query.

        Parameters:
        - query (str): The search query.

        Returns:
        - list: List of ranked search results.
        """
        matching_documents = self.get_matching_documents(query)
        ranked_results = self.rank_search_results(query, matching_documents)
        return ranked_results
