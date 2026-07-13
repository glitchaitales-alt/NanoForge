"""
Tests for the GenerationContext.
"""

import random

from nanoforge.datasets import (
    EntityFactory,
    GenerationContext,
)


def test_default_difficulty():
    """GenerationContext should default to difficulty 1."""

    context = GenerationContext(
        rng=random.Random(42),
        entity_factory=EntityFactory(seed=42),
    )

    assert context.difficulty == 1


def test_custom_difficulty():
    """GenerationContext should accept a custom difficulty."""

    context = GenerationContext(
        rng=random.Random(42),
        entity_factory=EntityFactory(seed=42),
        difficulty=5,
    )

    assert context.difficulty == 5


def test_entity_factory_exists():
    """GenerationContext should expose an EntityFactory."""

    context = GenerationContext(
        rng=random.Random(),
        entity_factory=EntityFactory(),
    )

    assert isinstance(context.entity_factory, EntityFactory)


def test_rng_exists():
    """GenerationContext should expose its RNG."""

    rng = random.Random(123)

    context = GenerationContext(
        rng=rng,
        entity_factory=EntityFactory(seed=123),
    )

    assert context.rng is rng