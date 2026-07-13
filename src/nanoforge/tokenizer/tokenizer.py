"""
NanoForge

Tokenizer Interface
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Tokenizer(ABC):
    """
    Base tokenizer interface.
    """

    @abstractmethod
    def train(self, text: str) -> None:
        """Train the tokenizer."""

    @abstractmethod
    def encode(self, text: str) -> list[int]:
        """Convert text into token IDs."""

    @abstractmethod
    def decode(self, ids: list[int]) -> str:
        """Convert token IDs back into text."""

    @abstractmethod
    def save(self, path: str) -> None:
        """Save tokenizer."""

    @classmethod
    @abstractmethod
    def load(cls, path: str):
        """Load tokenizer."""