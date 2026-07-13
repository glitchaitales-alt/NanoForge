import pytest

from nanoforge.datasets import (
    DatasetGenerator,
    Metadata,
    Message,
    Role,
    Sample,
    Task,
    TaskRegistry,
    GenerationContext,
)


class DummyTask(Task):

    name = "dummy"

    def generate(
        self,
        context: GenerationContext,
    ) -> Sample:

        return Sample(
            messages=[
                Message(
                    role=Role.USER,
                    content="Hello",
                )
            ],
            metadata=Metadata(
                task="dummy",
            ),
        )


def test_generate():

    registry = TaskRegistry()

    registry.register(DummyTask())

    generator = DatasetGenerator(
        registry
    )

    samples = list(
        generator.generate(
            count=5
        )
    )

    assert len(samples) == 5


def test_empty_registry():

    registry = TaskRegistry()

    generator = DatasetGenerator(
        registry
    )

    with pytest.raises(ValueError):
        list(
            generator.generate(
                count=1
            )
        )


def test_invalid_count():

    registry = TaskRegistry()

    registry.register(DummyTask())

    generator = DatasetGenerator(
        registry
    )

    with pytest.raises(ValueError):
        list(
            generator.generate(
                count=0
            )
        )


def test_returns_sample():

    registry = TaskRegistry()

    registry.register(DummyTask())

    generator = DatasetGenerator(
        registry
    )

    sample = next(
        generator.generate(
            count=1
        )
    )

    assert isinstance(
        sample,
        Sample,
    )