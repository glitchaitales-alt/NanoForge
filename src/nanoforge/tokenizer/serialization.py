"""
NanoForge

Tokenizer Serialization
"""

from __future__ import annotations

import json

from .merge_rule import MergeRule


def save_merges(
    merges: list[MergeRule],
    path: str,
) -> None:
    """
    Save learned merges to a JSON file.
    """

    data = [
        {
            "left": merge.left,
            "right": merge.right,
            "merged": merge.merged,
        }
        for merge in merges
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_merges(
    path: str,
) -> list[MergeRule]:
    """
    Load learned merges from a JSON file.
    """

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        MergeRule(
            left=item["left"],
            right=item["right"],
            merged=item["merged"],
        )
        for item in data
    ]