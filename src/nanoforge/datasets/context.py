"""
NanoForge

Generation Context

Shared state passed to every dataset task.
"""

from __future__ import annotations

from dataclasses import dataclass
import random

from .entities import EntityFactory


@dataclass(slots=True)
class GenerationContext:
    """
    Shared generation state.

    A single context is created by DatasetGenerator
    and passed into every task.
    """

    rng: random.Random

    entity_factory: EntityFactory

    difficulty: int = 1