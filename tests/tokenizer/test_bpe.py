from collections import Counter
from nanoforge.tokenizer.algorithms.bpe import BPETrainer
from nanoforge.tokenizer.merge_rule import MergeRule


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


def test_single_symbol_word():

    trainer = BPETrainer()

    counts = trainer.count_pairs(
        [
            ["A"],
        ]
    )

    assert counts == Counter()


def test_empty_counter():

    trainer = BPETrainer()

    assert trainer.most_frequent_pair(
        Counter()
    ) is None

def test_multiple_pairs():

    trainer = BPETrainer()

    counts = Counter({
        ("l", "o"): 5,
        ("o", "w"): 2,
        ("e", "r"): 1,
    })

    assert (
        trainer.most_frequent_pair(counts)
        == ("l", "o")
    )

def test_single_pair():

    trainer = BPETrainer()

    counts = Counter({
        ("l", "o"): 5,
    })

    assert (
        trainer.most_frequent_pair(counts)
        == ("l", "o")
    )

def test_merge_single_pair():

    trainer = BPETrainer()

    corpus = [
        [108, 111, 119],
    ]

    merged = trainer.merge_pair(
        corpus,
        (108, 111),
        256,
    )

    assert merged == [
        [256, 119],
    ]



def test_merge_multiple_occurrences():

    trainer = BPETrainer()

    corpus = [
        [1, 2, 1, 2],
    ]

    merged = trainer.merge_pair(
        corpus,
        (1, 2),
        256,
    )

    assert merged == [
        [256, 256],
    ]


def test_no_merge():

    trainer = BPETrainer()

    corpus = [
        [108, 111, 119],
    ]

    merged = trainer.merge_pair(
        corpus,
        (120, 121),
        256,
    )

    assert merged == corpus


def test_partial_merge():

    trainer = BPETrainer()

    corpus = [
        [108, 111, 119, 101],
    ]

    merged = trainer.merge_pair(
        corpus,
        (111, 119),
        256,
    )

    assert merged == [
        [108, 256, 101],
    ]

def test_train_zero_merges():

    trainer = BPETrainer()

    corpus = [
        ["l", "o", "w"],
    ]

    assert trainer.train(
        corpus,
        num_merges=0,
    ) == corpus

def test_train_one_merge():

    trainer = BPETrainer()

    corpus = [
        [108, 111, 119],
        [108, 111, 119, 101, 114],
    ]

    trained = trainer.train(
        corpus,
        num_merges=1,
    )

    assert trainer.merges == [
        MergeRule(
            left=108,
            right=111,
            merged=256,
        )
    ]

    assert trained == [
        [256, 119],
        [256, 119, 101, 114],
    ]

