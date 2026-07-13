import pytest

from nanoforge.tokenizer import Tokenizer


def test_tokenizer_is_abstract():

    with pytest.raises(TypeError):
        Tokenizer()