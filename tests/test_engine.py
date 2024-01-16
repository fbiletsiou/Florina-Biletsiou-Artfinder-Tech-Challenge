import pytest
from src.search_engine.engine import Engine
from src.search_engine.trie import TrieNode, insert_into_trie


@pytest.fixture
def sample_trie_root():
    # Create a sample Trie for testing
    root = TrieNode()
    insert_into_trie(root, "apple", "doc1.txt")
    insert_into_trie(root, "banana", "doc2.txt")
    insert_into_trie(root, "orange", "doc3.txt")
    return root


@pytest.fixture
def sample_document_contents():
    # Sample document contents for testing
    return [
        {'file_name': 'doc1.txt', 'content': 'This is an apple.'},
        {'file_name': 'doc2.txt', 'content': 'Banana is a yellow fruit.'},
        {'file_name': 'doc3.txt', 'content': 'Orange juice is refreshing.'},
    ]


def test_engine_init(sample_trie_root, sample_document_contents):
    engine = Engine(sample_trie_root, sample_document_contents)
    assert engine.trie_root == sample_trie_root
    assert engine.document_contents == sample_document_contents


def test_calculate_rank_score():
    query_tokens = ["apple", "orange"]
    document = "This is an apple and orange."
    score = Engine.calculate_rank_score(query_tokens, document)
    assert score == 100.0


def test_get_matching_documents(sample_trie_root):
    engine = Engine(sample_trie_root, [])
    matching_documents = engine.get_matching_documents("apple orange")
    assert matching_documents == {'doc1.txt', 'doc3.txt'}


def test_rank_search_results(sample_document_contents):
    engine = Engine(TrieNode(), sample_document_contents)
    matching_documents = {'doc1.txt', 'doc3.txt'}
    ranked_results = engine.rank_search_results("apple orange", matching_documents)
    assert ranked_results == [('doc1.txt', 50.0), ('doc3.txt', 50.0)]


def test_search(sample_trie_root, sample_document_contents):
    engine = Engine(sample_trie_root, sample_document_contents)
    results = engine.search("apple orange")
    assert results == [('doc1.txt', 50.0), ('doc3.txt', 50.0)]


def test_search_no_results(sample_trie_root, sample_document_contents):
    engine = Engine(sample_trie_root, sample_document_contents)
    results = engine.search("grape")
    assert results == []


def test_search_with_empty_query(sample_trie_root, sample_document_contents):
    engine = Engine(sample_trie_root, sample_document_contents)
    results = engine.search("")
    assert results == []


def test_search_with_invalid_query(sample_trie_root, sample_document_contents):
    engine = Engine(sample_trie_root, sample_document_contents)
    results = engine.search(None)
    assert results == []


def test_search_with_invalid_document_contents(sample_trie_root):
    engine = Engine(sample_trie_root, None)
    results = engine.search("apple")
    assert results == []


def test_search_with_invalid_trie_root(sample_document_contents):
    engine = Engine(None, sample_document_contents)
    results = engine.search("apple")
    assert results == []


def test_calculate_rank_score_no_intersection():
    query_tokens = ["apple", "orange"]
    document = "This is a banana."
    score = Engine.calculate_rank_score(query_tokens, document)
    assert score == 0.0
