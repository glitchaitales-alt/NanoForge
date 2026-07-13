"""
NanoForge

Task Registry

Stores and manages dataset tasks.
"""

from __future__ import annotations

from .task import Task


class TaskRegistry:
    """
    Registry for dataset tasks.

    Tasks are stored by their unique name.
    """

    def __init__(self) -> None:
        self._tasks: dict[str, Task] = {}

    def register(self, task: Task) -> None:
        """
        Register a task instance.
        """

        if task.name in self._tasks:
            raise ValueError(
                f"Task '{task.name}' is already registered."
            )

        self._tasks[task.name] = task

    def get(self, name: str) -> Task:
        """
        Retrieve a task by name.
        """

        try:
            return self._tasks[name]
        except KeyError:
            raise KeyError(
                f"Task '{name}' is not registered."
            ) from None

    def list(self) -> list[str]:
        """
        Return all registered task names.
        """

        return sorted(self._tasks.keys())

    def __contains__(self, name: str) -> bool:
        return name in self._tasks

    def __len__(self) -> int:
        return len(self._tasks)