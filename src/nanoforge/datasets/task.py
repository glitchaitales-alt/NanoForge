"""
Base dataset task.
"""

from abc import ABC, abstractmethod
from .context import GenerationContext
from .sample import Sample


class Task(ABC):

    name = "task"

    @abstractmethod
    def generate(
        self,
        context: GenerationContext,
    ) -> Sample:
        raise NotImplementedError