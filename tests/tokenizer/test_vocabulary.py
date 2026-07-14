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

def test_special_tokens_exist():

    vocab = Vocabulary.with_special_tokens()

    assert "<PAD>" in vocab
    assert "<UNK>" in vocab
    assert "<BOS>" in vocab
    assert "<EOS>" in vocab

def test_special_token_ids():

    vocab = Vocabulary.with_special_tokens()

    assert vocab.pad_id == 0
    assert vocab.unk_id == 1
    assert vocab.bos_id == 2
    assert vocab.eos_id == 3

def test_special_token_lookup():

    vocab = Vocabulary.with_special_tokens()

    assert vocab.token_to_id("<PAD>") == vocab.pad_id

    assert vocab.id_to_token(
        vocab.eos_id
    ) == "<EOS>"

def test_add_after_special_tokens():

    vocab = Vocabulary.with_special_tokens()

    token_id = vocab.add("hello")

    assert token_id == 4

def test_with_special_tokens():

    vocab = Vocabulary.with_special_tokens()

    assert vocab.pad_id == 0
    assert vocab.unk_id == 1
    assert vocab.bos_id == 2
    assert vocab.eos_id == 3