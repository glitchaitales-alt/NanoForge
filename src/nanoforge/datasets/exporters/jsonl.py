"""
NanoForge

JSONL Exporter
"""

from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path

from ..sample import Sample


class JsonlExporter:
    """
    Export samples to JSON Lines.
    """

    def _serialize(
        self,
        sample: Sample,
    ) -> dict:
        """
        Convert a Sample into a JSON-serializable dictionary.
        """

        return {
            "messages": [
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in sample.messages
            ],
            "metadata": {
                "task": sample.metadata.task,
                "difficulty": sample.metadata.difficulty,
                "entities": sample.metadata.entities,
                "expected_tool": sample.metadata.expected_tool,
                "expected_answer": sample.metadata.expected_answer,
                "tags": sample.metadata.tags,
            },
        }

    def write(
        self,
        samples: Iterable[Sample],
        output_path: str | Path,
    ) -> None:
        """
        Write samples to a JSONL file.
        """

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_path.open(
            "w",
            encoding="utf-8",
        ) as file:

            for sample in samples:
                json.dump(
                    self._serialize(sample),
                    file,
                    ensure_ascii=False,
                )
                file.write("\n")