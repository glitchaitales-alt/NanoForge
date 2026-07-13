import pytest

from nanoforge.datasets import Message, Role


def test_message_creation():

    msg = Message(
        role=Role.USER,
        content="Hello"
    )

    assert msg.role == Role.USER
    assert msg.content == "Hello"


def test_empty_message():

    with pytest.raises(ValueError):
        Message(
            role=Role.USER,
            content=""
        )