"""
NanoForge

Dataset Generator

Streams Sample objects from registered tasks.
"""

from __future__ import annotations

import random
from collections.abc import Iterator

from .context import GenerationContext
from .entities import EntityFactory
from .registry import TaskRegistry
from .sample import Sample


class DatasetGenerator:
    """
    Streams samples from registered tasks.
    """

    def __init__(
        self,
        registry: TaskRegistry,
        seed: int | None = None,
    ) -> None:

        self.registry = registry

        self.random = random.Random(seed)

        self.entity_factory = EntityFactory(seed)

    def generate(
        self,
        count: int,
    ) -> Iterator[Sample]:

        if count < 1:
            raise ValueError(
                "count must be >= 1."
            )

        task_names = self.registry.list()

        if not task_names:
            raise ValueError(
                "No tasks are registered."
            )

        context = GenerationContext(
            rng=self.random,
            entity_factory=self.entity_factory,
        )

        for _ in range(count):

            task_name = self.random.choice(task_names)

            task = self.registry.get(task_name)

            yield task.generate(context)