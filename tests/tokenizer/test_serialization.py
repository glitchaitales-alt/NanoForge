from nanoforge.tokenizer import (
    BPETrainer,
)


def test_save_and_load(tmp_path):

    trainer = BPETrainer()

    trainer.train(
        [
            [108, 111, 119],
        ],
        num_merges=2,
    )

    path = tmp_path / "tokenizer.json"

    trainer.save(str(path))

    loaded = BPETrainer.load(
        str(path),
    )

    assert loaded.merges == trainer.merges