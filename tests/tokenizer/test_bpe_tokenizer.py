from nanoforge.tokenizer import (
    BPETrainer,
    BPETokenizer,
)


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