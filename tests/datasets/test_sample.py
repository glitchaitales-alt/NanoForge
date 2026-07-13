import pytest

from nanoforge.datasets import (
    Sample,
    Message,
    Metadata,
    Role,
)


def test_sample():

    sample = Sample(
        messages=[
            Message(
                Role.USER,
                "Hello"
            )
        ],
        metadata=Metadata(
            task="copy"
        ),
    )

    assert len(sample.messages) == 1


def test_empty_sample():

    with pytest.raises(ValueError):
        Sample(
            messages=[],
            metadata=Metadata(task="copy")
        )