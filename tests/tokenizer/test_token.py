from dataclasses import FrozenInstanceError

import pytest

from nanoforge.tokenizer import Token


def test_token_fields():

    token = Token(
        id=0,
        text="hello",
    )

    assert token.id == 0
    assert token.text == "hello"


def test_token_is_immutable():

    token = Token(
        id=0,
        text="hello",
    )

    with pytest.raises(FrozenInstanceError):
        token.text = "world"