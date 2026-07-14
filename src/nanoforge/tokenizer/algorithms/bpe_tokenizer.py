"""
NanoForge

Byte Pair Encoding Tokenizer
"""

from __future__ import annotations

from ..merge_rule import MergeRule
from .byte import ByteTokenizer


class BPETokenizer:
    """
    Applies learned BPE merges to text.
    """

    def __init__(
        self,
        merges: list[MergeRule],
    ) -> None:

        self._merges = merges
        self._byte_tokenizer = ByteTokenizer()

    def encode(
        self,
        text: str,
    ) -> list[int]:

        tokens = self._byte_tokenizer.encode(text)

        for merge in self._merges:

            merged_tokens = []

            i = 0

            while i < len(tokens):

                if (
                    i < len(tokens) - 1
                    and tokens[i] == merge.left
                    and tokens[i + 1] == merge.right
                ):
                    merged_tokens.append(
                        merge.merged
                    )

                    i += 2

                else:

                    merged_tokens.append(
                        tokens[i]
                    )

                    i += 1

            tokens = merged_tokens

        return tokens