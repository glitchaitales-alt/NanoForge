"""
NanoForge

Tokenizer Exceptions
"""


class TokenizerError(Exception):
    """Base tokenizer exception."""


class VocabularyError(TokenizerError):
    """Raised for vocabulary errors."""


class UnknownTokenError(VocabularyError):
    """Raised when a token cannot be found."""