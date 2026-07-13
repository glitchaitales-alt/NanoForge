import pytest

from nanoforge.datasets import (
    Metadata,
    Message,
    Role,
    Sample,
    Task,
    TaskRegistry,
)


class DummyTask(Task):

    name = "dummy"

    def generate(self):

        return Sample(
            messages=[
                Message(
                    Role.USER,
                    "Hello"
                )
            ],
            metadata=Metadata(
                task="dummy"
            ),
        )


def test_register():

    registry = TaskRegistry()

    registry.register(DummyTask())

    assert len(registry) == 1


def test_get():

    registry = TaskRegistry()

    registry.register(DummyTask())

    task = registry.get("dummy")

    assert task.name == "dummy"


def test_duplicate_registration():

    registry = TaskRegistry()

    registry.register(DummyTask())

    with pytest.raises(ValueError):
        registry.register(DummyTask())


def test_missing_task():

    registry = TaskRegistry()

    with pytest.raises(KeyError):
        registry.get("missing")


def test_contains():

    registry = TaskRegistry()

    registry.register(DummyTask())

    assert "dummy" in registry


def test_list():

    registry = TaskRegistry()

    registry.register(DummyTask())

    assert registry.list() == ["dummy"]