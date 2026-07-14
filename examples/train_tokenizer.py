"""
NanoForge

End-to-End Tokenizer Example
"""

from nanoforge.tokenizer import (
    BPETrainer,
    BPETokenizer,
)


def main() -> None:

    corpus = [
        "NanoForge builds language models.",
        "NanoForge trains tokenizers.",
        "Language models learn from data.",
        "Tokenizers split text into tokens.",
    ]

    trainer = BPETrainer()

    trainer.train_from_text(
        corpus,
        num_merges=25,
    )

    trainer.save("tokenizer.json")

    print("✓ Tokenizer trained.")
    print("✓ Merge rules:", len(trainer.merges))

    loaded = BPETrainer.load(
        "tokenizer.json",
    )

    tokenizer = BPETokenizer(
        loaded.merges,
    )

    text = "NanoForge"

    encoded = tokenizer.encode(text)

    decoded = tokenizer.decode(encoded)

    print()
    print("Input   :", text)
    print("Encoded :", encoded)
    print("Decoded :", decoded)


if __name__ == "__main__":
    main()