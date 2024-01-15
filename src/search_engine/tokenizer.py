import re


def tokenize(content):
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', content.lower())
    # Split on whitespace
    tokens = text.split()
    return tokens
