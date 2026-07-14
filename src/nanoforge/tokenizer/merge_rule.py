from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class MergeRule:
    """
    Represents a learned BPE merge.
    """

    left: int
    right: int
    merged: int