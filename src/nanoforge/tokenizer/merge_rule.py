"""
NanoForge

BPE Merge Rule
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MergeRule:
    """
    Represents a single BPE merge operation.
    """

    left: str
    right: str
    merged: str