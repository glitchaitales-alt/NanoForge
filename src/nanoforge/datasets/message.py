"""
NanoForge

Message abstraction used throughout the dataset pipeline.
"""

from dataclasses import dataclass
from enum import Enum


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"
    THOUGHT = "thought"


@dataclass(frozen=True, slots=True)
class Message:
    """
    Represents one conversational message.
    """

    role: Role
    content: str

    def __post_init__(self):
        if not self.content.strip():
            raise ValueError("Message content cannot be empty.")