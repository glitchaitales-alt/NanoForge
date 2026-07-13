"""
Metadata attached to every generated sample.
"""

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Metadata:

    task: str

    difficulty: int = 1

    entities: list[str] = field(default_factory=list)

    expected_tool: str | None = None

    expected_answer: str = ""

    tags: list[str] = field(default_factory=list)

    def __post_init__(self):

        if self.difficulty < 1:
            raise ValueError(
                "Difficulty must be >= 1."
            )