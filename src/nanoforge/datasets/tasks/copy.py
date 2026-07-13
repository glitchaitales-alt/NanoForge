"""
NanoForge

Copy Task
"""

from __future__ import annotations

from ..context import GenerationContext
from ..metadata import Metadata
from ..message import Message, Role
from ..prompts import COPY_PROMPTS
from ..sample import Sample
from .base import Task


class CopyTask(Task):
    """
    Generate copy-style training samples.
    """

    name = "copy"

    description = "Copy text exactly."

    def generate(
        self,
        context: GenerationContext,
    ) -> Sample:

        entity_generator = context.rng.choice(
            (
                context.entity_factory.customer_id,
                context.entity_factory.invoice,
                context.entity_factory.email,
                context.entity_factory.uuid,
                context.entity_factory.full_name,
            )
        )

        value = entity_generator()

        template = context.rng.choice(COPY_PROMPTS)

        prompt = template.format(value)

        return Sample(
            messages=(
                Message(
                    role=Role.USER,
                    content=prompt,
                ),
            ),
            metadata=Metadata(
                task=self.name,
                difficulty=context.difficulty,
                expected_answer=value,
            ),
        )