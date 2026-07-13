"""
Tests for the JSONL exporter.
"""

from __future__ import annotations

import json

from nanoforge.datasets import (
    JsonlExporter,
    Message,
    Metadata,
    Role,
    Sample,
)


def make_sample() -> Sample:
    """
    Create a reusable sample for exporter tests.
    """

    return Sample(
        messages=(
            Message(
                role=Role.USER,
                content="Copy this exactly:\n\nABC-12345",
            ),
        ),
        metadata=Metadata(
            task="copy",
            difficulty=1,
            expected_answer="ABC-12345",
        ),
    )


def test_write_creates_file(tmp_path):
    exporter = JsonlExporter()

    output = tmp_path / "dataset.jsonl"

    exporter.write(
        [make_sample()],
        output,
    )

    assert output.exists()


def test_single_sample_written(tmp_path):
    exporter = JsonlExporter()

    output = tmp_path / "dataset.jsonl"

    exporter.write(
        [make_sample()],
        output,
    )

    lines = output.read_text(
        encoding="utf-8",
    ).splitlines()

    assert len(lines) == 1


def test_valid_json(tmp_path):
    exporter = JsonlExporter()

    output = tmp_path / "dataset.jsonl"

    exporter.write(
        [make_sample()],
        output,
    )

    line = output.read_text(
        encoding="utf-8",
    ).strip()

    data = json.loads(line)

    assert isinstance(data, dict)


def test_role_serialized(tmp_path):
    exporter = JsonlExporter()

    output = tmp_path / "dataset.jsonl"

    exporter.write(
        [make_sample()],
        output,
    )

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    assert data["messages"][0]["role"] == "user"


def test_metadata_serialized(tmp_path):
    exporter = JsonlExporter()

    output = tmp_path / "dataset.jsonl"

    exporter.write(
        [make_sample()],
        output,
    )

    data = json.loads(
        output.read_text(
            encoding="utf-8",
        )
    )

    metadata = data["metadata"]

    assert metadata["task"] == "copy"

    assert metadata["difficulty"] == 1

    assert metadata["expected_answer"] == "ABC-12345"


def test_empty_iterable(tmp_path):
    exporter = JsonlExporter()

    output = tmp_path / "dataset.jsonl"

    exporter.write(
        [],
        output,
    )

    assert output.exists()

    assert output.read_text(
        encoding="utf-8",
    ) == ""