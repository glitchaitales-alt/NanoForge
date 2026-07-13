"""
Sample object used throughout NanoForge.
"""

from dataclasses import dataclass

from .message import Message
from .metadata import Metadata


@dataclass(frozen=True, slots=True)
class Sample:

    messages: list[Message]

    metadata: Metadata

    def __post_init__(self):

        if len(self.messages) == 0:
            raise ValueError(
                "Sample requires at least one message."
            )