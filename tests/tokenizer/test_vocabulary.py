import pytest

from nanoforge.tokenizer import (
    UnknownTokenError,
    Vocabulary,
)


def test_empty_vocabulary():

    vocab = Vocabulary()

    assert len(vocab) == 0


def test_add_token():

    vocab = Vocabulary()

    token_id = vocab.add("hello")

    assert token_id == 0
    assert len(vocab) == 1


def test_duplicate_token_returns_same_id():

    vocab = Vocabulary()

    first = vocab.add("hello")
    second = vocab.add("hello")

    assert first == second
    assert len(vocab) == 1


def test_token_lookup():

    vocab = Vocabulary()

    vocab.add("hello")

    assert vocab.token_to_id("hello") == 0


def test_id_lookup():

    vocab = Vocabulary()

    vocab.add("hello")

    assert vocab.id_to_token(0) == "hello"


def test_unknown_token():

    vocab = Vocabulary()

    with pytest.raises(UnknownTokenError):
        vocab.token_to_id("missing")


def test_unknown_id():

    vocab = Vocabulary()

    with pytest.raises(UnknownTokenError):
        vocab.id_to_token(99)