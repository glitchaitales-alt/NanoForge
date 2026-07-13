"""
NanoForge

EntityFactory

Provides deterministic generators for synthetic entities.
"""

from __future__ import annotations

import random
import string


class EntityFactory:
    """
    Generates synthetic entities for dataset creation.

    Every generator uses an internal Random instance,
    making output reproducible when a seed is supplied.
    """

    CITIES = (
        "Tokyo",
        "London",
        "Berlin",
        "Paris",
        "Mumbai",
        "Bangalore",
        "Sydney",
        "Toronto",
    )

    FIRST_NAMES = (
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Emma",
        "Sophia",
        "Olivia",
        "Liam",
    )

    LAST_NAMES = (
        "Smith",
        "Johnson",
        "Brown",
        "Wilson",
        "Taylor",
        "Davis",
    )

    def __init__(self, seed: int | None = None):

        self.random = random.Random(seed)

    def customer_id(self) -> str:

        prefix = "".join(
            self.random.choice(string.ascii_uppercase)
            for _ in range(3)
        )

        suffix = self.random.randint(10000, 99999)

        return f"{prefix}-{suffix}"

    def invoice(self) -> str:

        return f"INV-{self.random.randint(100000,999999)}"

    def uuid(self) -> str:

        alphabet = string.ascii_uppercase + string.digits

        groups = []

        for _ in range(4):

            groups.append(
                "".join(
                    self.random.choice(alphabet)
                    for _ in range(4)
                )
            )

        return "-".join(groups)

    def city(self) -> str:

        return self.random.choice(self.CITIES)

    def full_name(self) -> str:

        return (
            f"{self.random.choice(self.FIRST_NAMES)} "
            f"{self.random.choice(self.LAST_NAMES)}"
        )

    def email(self) -> str:

        first = self.random.choice(self.FIRST_NAMES).lower()

        last = self.random.choice(self.LAST_NAMES).lower()

        domain = self.random.choice(
            (
                "gmail.com",
                "example.com",
                "company.com",
            )
        )

        number = self.random.randint(1,999)

        return f"{first}.{last}{number}@{domain}"