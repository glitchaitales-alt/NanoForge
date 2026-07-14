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
        self._decode_map = {
        merge.merged: (merge.left, merge.right)
        for merge in merges
        }

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
    
    def _expand_token(
        self,
        token: int,
    ) -> list[int]:
        """
        Recursively expand a merged token into its original bytes.
        """

        if token < 256:
            return [token]

        left, right = self._decode_map[token]

        return (
            self._expand_token(left)
            + self._expand_token(right)
        )
    
    def decode(
        self,
        tokens: list[int],
    ) -> str:
        """
        Decode token IDs back into text.
        """

        bytes_out = []

        for token in tokens:
            bytes_out.extend(
                self._expand_token(token)
            )

        return bytes(bytes_out).decode("utf-8")
        