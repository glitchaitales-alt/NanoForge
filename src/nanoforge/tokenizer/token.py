"""
NanoForge

Token

Represents a single vocabulary token.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Token:
    """
    Represents a vocabulary token.
    """

    id: int
    text: str