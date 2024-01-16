import pytest

from src.search_engine.trie import TrieNode, insert_into_trie, build_trie


@pytest.fixture
def sample_file_data():
    return [
        {'file_name': 'doc1.txt', 'content': 'sample content for doc1'},
        {'file_name': 'doc2.txt', 'content': 'sample content for doc2'},
    ]


@pytest.fixture
def root():
    return TrieNode()


def test_insert_into_trie_adds_documents_to_node(root):
    insert_into_trie(root, 'sample', 'doc1.txt')

    assert root.children['s'].children['a'].children['m'].children['p'].children['l'].children['e'].documents == {'doc1.txt'}


def test_insert_into_trie_handles_empty_word(root):
    insert_into_trie(root, '', 'doc1.txt')

    assert root.documents == {'doc1.txt'}


def test_build_trie_creates_valid_trie(sample_file_data):
    root = build_trie(sample_file_data)

    # Check if Trie contains words from the documents
    assert 'doc1.txt' in root.children['s'].children['a'].children['m'].children['p'].children['l'].children['e'].documents
    assert 'doc2.txt' in root.children['s'].children['a'].children['m'].children['p'].children['l'].children['e'].documents
    assert 'doc1.txt' in root.children['c'].children['o'].children['n'].children['t'].children['e'].children['n'].children['t'].documents
    assert 'doc2.txt' in root.children['c'].children['o'].children['n'].children['t'].children['e'].children['n'].children['t'].documents


def test_build_trie_handles_empty_file_data():
    root = build_trie([])

    assert root.children == {}


def test_build_trie_handles_empty_content_in_file_data():
    file_data = [{'file_name': 'doc1.txt', 'content': ''}]
    root = build_trie(file_data)

    assert root.documents == set()


def test_build_trie_handles_non_string_content_in_file_data(sample_file_data):
    sample_file_data[0]['content'] = None
    root = build_trie(sample_file_data[:1])

    assert root.children == {}
