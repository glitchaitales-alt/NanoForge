"""
NanoForge

Vocabulary Builder
"""

from __future__ import annotations

from collections.abc import Iterable

from .vocabulary import Vocabulary


class VocabularyBuilder:
    """
    Builds a vocabulary from token sequences.
    """

    def build(
        self,
        token_sequences: Iterable[list[int]],
    ) -> Vocabulary:

        vocab = Vocabulary()

        for sequence in token_sequences:

            for token in sequence:

                vocab.add(str(token))

        return vocab