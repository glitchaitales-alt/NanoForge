# ADR 0002 — Dataset Architecture

## Status

Accepted

---

## Context

Dataset generation is the first stage of the NanoForge pipeline.

Future tokenizers and trainers will consume these datasets.

---

## Decision

Dataset generation is separated into distinct responsibilities.

- Tasks create samples.
- DatasetGenerator orchestrates generation.
- EntityFactory creates deterministic entities.
- Exporters serialize datasets.

---

## Consequences

### Positive

- Highly modular
- Easy to extend
- Easy to test

### Negative

- Slightly more files
- Additional abstraction