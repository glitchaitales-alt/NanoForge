from nanoforge.datasets import (
    Task,
    Sample,
    Metadata,
    Message,
    Role,
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
            metadata=Metadata(task="dummy"),
        )


def test_task():

    task = DummyTask()

    sample = task.generate()

    assert sample.metadata.task == "dummy"