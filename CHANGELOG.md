# Changelog

All notable changes to NanoForge are documented in this file.

The format is inspired by **Keep a Changelog** and follows **Semantic Versioning**.

---

# [Unreleased]

## Planned

### Added

- GitHub Actions
- Ruff linting
- Formatting configuration
- Architecture Decision Records (ADRs)

---

# [0.2.0] - Foundations (In Progress)

## Added

### Dataset System

- Core dataset objects
- Message model
- Metadata model
- Sample model
- Task abstraction

### Generation

- Deterministic entity generation
- Streaming dataset generator
- Generation context
- Task registry

### Tasks

- Prompt template system
- CopyTask

### Exporters

- JSONL exporter

### Examples

- Dataset generation example

### Documentation

- README
- ROADMAP

### Engineering

- Feature branch workflow
- Conventional commits
- Expanded unit test coverage

---

# [0.1.0] - Genesis

Initial release.

## Added

- Project structure
- Python packaging
- Editable installation
- CLI entry point
- Test framework

## [0.3.0] - 2026-07-14

### Added
- Byte Pair Encoding (BPE) trainer
- Byte-level tokenizer
- BPE tokenizer inference
- Tokenizer serialization
- Bidirectional encoding/decoding
- High-level text training API
- Vocabulary management
- Special token support
- End-to-end tokenizer example

### Changed
- Migrated BPE training from character-level to byte-level tokens.

### Tests
- 94 automated tests passing.