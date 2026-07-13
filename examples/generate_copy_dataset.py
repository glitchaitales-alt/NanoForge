"""
NanoForge Example

Generate a small copy dataset.
"""

from pathlib import Path

from nanoforge.datasets import (
    CopyTask,
    DatasetGenerator,
    JsonlExporter,
    TaskRegistry,
)


def main() -> None:
    registry = TaskRegistry()

    registry.register(CopyTask())

    generator = DatasetGenerator(
        registry=registry,
        seed=42,
    )

    exporter = JsonlExporter()

    output = Path("datasets") / "copy_dataset.jsonl"

    exporter.write(
        generator.generate(count=100),
        output,
    )

    print("=" * 50)
    print("NanoForge Dataset Generation")
    print("=" * 50)
    print(f"Generated 100 samples")
    print(f"Saved to: {output}")
    print("=" * 50)


if __name__ == "__main__":
    main()