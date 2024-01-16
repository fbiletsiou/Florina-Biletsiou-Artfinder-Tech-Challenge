import pytest

from src.search_engine.tokenizer import tokenize


def test_tokenize_returns_list():
    result = tokenize("This is a test.")
    assert isinstance(result, list)


def test_tokenize_removes_punctuation():
    result = tokenize("Hello, world!")
    assert result == ['hello', 'world']
    assert '!' not in result
    assert ',' not in result


def test_tokenize_converts_to_lowercase():
    result = tokenize("Hello World")
    assert result == ['hello', 'world']
    assert 'Hello' not in result
    assert 'world' in result


def test_tokenize_handles_empty_string():
    result = tokenize("")
    assert result == []


def test_tokenize_requires_string_input():
    result = tokenize(123)
    assert result == []


def test_tokenize_handles_non_string_punctuation():
    result = tokenize(None)
    assert result == []
