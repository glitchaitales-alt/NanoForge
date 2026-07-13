import pytest

from nanoforge.datasets import Metadata


def test_metadata():

    meta = Metadata(task="copy")

    assert meta.task == "copy"
    assert meta.difficulty == 1


def test_invalid_difficulty():

    with pytest.raises(ValueError):
        Metadata(
            task="copy",
            difficulty=0
        )