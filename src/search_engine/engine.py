
from .trie import TrieNode
from .tokenizer import tokenize


class Engine:
    def __init__(self, trie_root: TrieNode, document_contents: list):
        self.trie_root = trie_root
        self.document_contents = document_contents

    @staticmethod
    def calculate_rank_score(query_tokens: list, document: str) -> float:
        document_words = tokenize(document)
        intersection = set(query_tokens) & set(document_words)

        if not intersection:
            return 0.0

        if set(query_tokens) == intersection:
            return 100.0

        return len(intersection) / len(set(query_tokens)) * 100.0

    def get_matching_documents(self, query: str) -> set:
        # Tokenize the query
        query_tokens = tokenize(query)

        matching_documents = set()
        node = self.trie_root

        for word in query_tokens:
            for char in word:
                if char in node.children:
                    node = node.children[char]
                else:
                    break
            else:
                # The inner loop completed without breaking, meaning the entire word was found
                matching_documents.update(node.documents)
                node = self.trie_root  # Reset to the root for the next word

        return matching_documents

    def rank_search_results(self, query: str, matching_documents: set) -> list:
        # Tokenize the query
        query_tokens = tokenize(query)

        ranked_results = []

        for document_data in self.document_contents:
            file_name = document_data['file_name']
            content = document_data['content']

            if file_name in matching_documents:
                score = self.calculate_rank_score(query_tokens, content)
                ranked_results.append((file_name, score))

        # Sort results by score in descending order
        ranked_results.sort(key=lambda x: x[1], reverse=True)

        return ranked_results[:10]  # Return top 10 results

    def search(self, query):
        matching_documents = self.get_matching_documents(query)
        ranked_results = self.rank_search_results(query, matching_documents)
        return ranked_results
