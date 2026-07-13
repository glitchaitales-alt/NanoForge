import random

from nanoforge.datasets import (
    CopyTask,
    EntityFactory,
    GenerationContext,
    Sample,
)


def make_context(seed: int = 42) -> GenerationContext:
    return GenerationContext(
        rng=random.Random(seed),
        entity_factory=EntityFactory(seed=seed),
    )


def test_generate_returns_sample():
    task = CopyTask()

    sample = task.generate(make_context())

    assert isinstance(sample, Sample)


def test_metadata_task_name():
    task = CopyTask()

    sample = task.generate(make_context())

    assert sample.metadata.task == "copy"


def test_expected_answer_present():
    task = CopyTask()

    sample = task.generate(make_context())

    assert sample.metadata.expected_answer in sample.messages[0].content


def test_same_seed_is_deterministic():
    task = CopyTask()

    sample1 = task.generate(make_context(123))
    sample2 = task.generate(make_context(123))

    assert sample1 == sample2


def test_prompt_is_not_empty():
    task = CopyTask()

    sample = task.generate(make_context())

    assert sample.messages[0].content.strip()