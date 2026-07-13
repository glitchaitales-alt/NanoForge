# ADR 0003 — Streaming Dataset Generation

## Status

Accepted

---

## Context

Large synthetic datasets may contain millions of samples.

Loading all samples into memory is inefficient.

---

## Decision

DatasetGenerator returns an iterator instead of a list.

Samples are generated lazily.

---

## Consequences

### Positive

- Constant memory usage
- Scales to large datasets
- Supports streaming exporters

### Negative

- Random access is unavailable