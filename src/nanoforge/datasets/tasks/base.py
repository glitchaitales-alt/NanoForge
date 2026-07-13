"""
NanoForge

Base task interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from ..context import GenerationContext
from ..sample import Sample


class Task(ABC):
    """
    Base class for all dataset tasks.
    """

    name = "task"

    description = "Base dataset task."

    @abstractmethod
    def generate(
        self,
        context: GenerationContext,
    ) -> Sample:
        """
        Generate a single training sample.

        Args:
            context:
                Shared generation context.

        Returns:
            Generated Sample.
        """
        raise NotImplementedError