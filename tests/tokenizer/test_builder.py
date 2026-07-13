from nanoforge.tokenizer import (
    Vocabulary,
    VocabularyBuilder,
)


def test_empty_input():

    builder = VocabularyBuilder()

    vocab = builder.build([])

    assert isinstance(vocab, Vocabulary)

    assert len(vocab) == 0

def test_single_sequence():

    builder = VocabularyBuilder()

    vocab = builder.build(
        [
            [65, 66, 67],
        ]
    )

    assert len(vocab) == 3


def test_duplicate_tokens():

    builder = VocabularyBuilder()

    vocab = builder.build(
        [
            [65, 66],
            [65],
        ]
    )

    assert len(vocab) == 2

def test_first_appearance_order():

    builder = VocabularyBuilder()

    vocab = builder.build(
        [
            [66, 65],
        ]
    )

    assert vocab.token_to_id("66") == 0

    assert vocab.token_to_id("65") == 1