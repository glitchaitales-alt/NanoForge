"""
Base dataset task.
"""

from abc import ABC, abstractmethod

from .sample import Sample


class Task(ABC):

    name = "task"

    @abstractmethod
    def generate(self) -> Sample:
        """
        Generate one sample.
        """
        raise NotImplementedError