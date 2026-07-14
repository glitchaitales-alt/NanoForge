"""
NanoForge

Vocabulary

Bidirectional mapping between token text and token IDs.
"""

from __future__ import annotations

from .exceptions import (
    UnknownTokenError,
    VocabularyError,
)


class Vocabulary:
    """
    Stores a bidirectional mapping between
    token text and token IDs.
    """

    def __init__(self) -> None:

        self._token_to_id: dict[str, int] = {}
        self._id_to_token: dict[int, str] = {}

    @classmethod
    def with_special_tokens(cls) -> "Vocabulary":
        """
        Create a vocabulary pre-populated with the
        standard special tokens used by NanoForge.
        """

        vocab = cls()

        vocab.pad_id = vocab.add("<PAD>")
        vocab.unk_id = vocab.add("<UNK>")
        vocab.bos_id = vocab.add("<BOS>")
        vocab.eos_id = vocab.add("<EOS>")

        return vocab

    def add(
        self,
        token: str,
    ) -> int:
        """
        Add a token to the vocabulary.

        Returns its ID.
        """

        if not token:
            raise VocabularyError(
                "Token cannot be empty."
            )

        if token in self._token_to_id:
            return self._token_to_id[token]

        token_id = len(self._token_to_id)

        self._token_to_id[token] = token_id
        self._id_to_token[token_id] = token

        return token_id

    def token_to_id(
        self,
        token: str,
    ) -> int:
        """
        Return the ID of a token.
        """

        try:
            return self._token_to_id[token]

        except KeyError as exc:
            raise UnknownTokenError(
                f"Unknown token: {token!r}"
            ) from exc

    def id_to_token(
        self,
        token_id: int,
    ) -> str:
        """
        Return the token for an ID.
        """

        try:
            return self._id_to_token[token_id]

        except KeyError as exc:
            raise UnknownTokenError(
                f"Unknown token id: {token_id}"
            ) from exc

    @property
    def pad_token(self) -> str:
        return "<PAD>"

    @property
    def unk_token(self) -> str:
        return "<UNK>"

    @property
    def bos_token(self) -> str:
        return "<BOS>"

    @property
    def eos_token(self) -> str:
        return "<EOS>"

    def __contains__(
        self,
        token: str,
    ) -> bool:

        return token in self._token_to_id

    def __len__(
        self,
    ) -> int:

        return len(self._token_to_id)