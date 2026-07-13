"""
NanoForge

Text Normalizer
"""

from __future__ import annotations


class TextNormalizer:
    """
    Cleans raw text before tokenization.
    """

    def normalize(
        self,
        text: str,
    ) -> str:

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Process each line independently
        lines = []

        for line in text.split("\n"):
            line = " ".join(line.split())
            lines.append(line)

        return "\n".join(lines).strip()