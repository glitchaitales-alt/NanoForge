from nanoforge.tokenizer import (
    BPETrainer,
    BPETokenizer,
)

def test_decode_without_merges():

    tokenizer = BPETokenizer([])

    assert tokenizer.decode(
        [65, 66, 67]
    ) == "ABC"

def test_decode_single_merge():

    trainer = BPETrainer()

    trainer.train(
        [
            [108, 111, 119],
        ],
        num_merges=1,
    )

    tokenizer = BPETokenizer(
        trainer.merges,
    )

    assert tokenizer.decode(
        [256, 119]
    ) == "low"

def test_decode_two_merges():

    trainer = BPETrainer()

    trainer.train(
        [
            [108, 111, 119],
        ],
        num_merges=2,
    )

    tokenizer = BPETokenizer(
        trainer.merges,
    )

    assert tokenizer.decode(
        [257]
    ) == "low"


def test_round_trip():

    trainer = BPETrainer()

    trainer.train(
        [
            [108, 111, 119],
            [108, 111, 119, 101, 114],
        ],
        num_merges=2,
    )

    tokenizer = BPETokenizer(
        trainer.merges,
    )

    text = "lower"

    encoded = tokenizer.encode(text)

    decoded = tokenizer.decode(encoded)

    assert decoded == text


def test_encode_without_merges():

    tokenizer = BPETokenizer([])

    assert tokenizer.encode("ABC") == [
        65,
        66,
        67,
    ]


def test_encode_single_merge():

    trainer = BPETrainer()

    trainer.train(
        [
            [108, 111, 119],
        ],
        num_merges=1,
    )

    tokenizer = BPETokenizer(
        trainer.merges,
    )

    assert tokenizer.encode("low") == [
        256,
        119,
    ]


def test_encode_two_merges():

    trainer = BPETrainer()

    trainer.train(
        [
            [108, 111, 119],
        ],
        num_merges=2,
    )

    tokenizer = BPETokenizer(
        trainer.merges,
    )

    assert tokenizer.encode("low") == [
        257,
    ]