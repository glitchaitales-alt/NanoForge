# ADR 0004 — Shared Generation Context

## Status

Accepted

---

## Context

Tasks require shared state such as randomness, entity generation, and future configuration.

Passing many independent parameters would make the API difficult to maintain.

---

## Decision

Introduce a GenerationContext object shared by all tasks.

The context contains:

- Random number generator
- EntityFactory
- Difficulty level

Future shared resources can be added without changing the Task interface.

---

## Consequences

### Positive

- Stable API
- Easy extensibility
- Cleaner task implementations

### Negative

- One additional abstraction