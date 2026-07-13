"""
NanoForge

Byte Tokenizer
"""

from __future__ import annotations

from ..tokenizer import Tokenizer


class ByteTokenizer(Tokenizer):
    """
    UTF-8 byte tokenizer.
    """

    def train(
        self,
        text: str,
    ) -> None:
        """
        Byte tokenizers require no training.
        """
        return None

    def encode(
        self,
        text: str,
    ) -> list[int]:

        return list(text.encode("utf-8"))

    def decode(
        self,
        ids: list[int],
    ) -> str:

        return bytes(ids).decode("utf-8")

    def save(
        self,
        path: str,
    ) -> None:

        raise NotImplementedError

    @classmethod
    def load(
        cls,
        path: str,
    ) -> "ByteTokenizer":

        raise NotImplementedError