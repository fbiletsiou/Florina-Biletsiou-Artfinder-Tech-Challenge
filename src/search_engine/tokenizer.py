import re


def tokenize(content: str) -> list:
    """
    Tokenizes the given content by removing punctuation, converting to lowercase,
    and splitting on whitespace.

    Parameters:
    - content (str): The input text to be tokenized.

    Returns:
    - list: A list of tokens.
    """
    try:
        # Ensure the input is a string
        if not isinstance(content, str):
            raise ValueError("Input must be a string.")

        # Remove punctuation and convert to lowercase
        text_without_punctuation = re.sub(r'[^\w\s]', '', content.lower())
        # Split on whitespace
        tokens = text_without_punctuation .split()

        return tokens
    except Exception as e:
        print(f"Error during tokenization: {e}")
        return []
