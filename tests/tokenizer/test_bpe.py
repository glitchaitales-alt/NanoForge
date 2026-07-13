from nanoforge.tokenizer.algorithms.bpe import BPETrainer


def test_empty_corpus():

    trainer = BPETrainer()

    counts = trainer.count_pairs([])

    assert counts == {}

def test_single_word():

    trainer = BPETrainer()

    counts = trainer.count_pairs(
        [
            ["l", "o", "w"],
        ]
    )

    assert counts == {
        ("l", "o"): 1,
        ("o", "w"): 1,
    }

def test_multiple_words():

    trainer = BPETrainer()

    counts = trainer.count_pairs(
        [
            ["l", "o", "w"],
            ["l", "o", "w"],
        ]
    )

    assert counts[("l", "o")] == 2

    assert counts[("o", "w")] == 2

    
def test_different_words():

    trainer = BPETrainer()

    counts = trainer.count_pairs(
        [
            ["n", "e", "w"],
            ["l", "o", "w"],
        ]
    )

    assert counts[("n", "e")] == 1

    assert counts[("e", "w")] == 1

    assert counts[("l", "o")] == 1

    assert counts[("o", "w")] == 1