# NanoForge Roadmap

> **Build. Understand. Engineer.**

This roadmap outlines the planned evolution of NanoForge.

The goal is to build a complete educational AI engineering framework, starting with dataset generation and progressing toward modern language models and AI agents.

---

# Guiding Principles

NanoForge is built around a few core principles.

- Build every major component from first principles.
- Favor readability over cleverness.
- Prefer composition over inheritance.
- Every feature is covered by automated tests.
- Every release leaves the project in a stable state.

---

# Version Roadmap

## ✅ v0.1.0 — Genesis

Initial project setup.

### Completed

- Project structure
- Python packaging
- Testing framework
- Initial CLI entry point

---

## 🚧 v0.2.0 — Foundations

Build the synthetic dataset pipeline.

### Completed

- Dataset core objects
- Entity factory
- Task registry
- Streaming dataset generator
- Generation context
- Task system
- Prompt templates
- Copy task
- JSONL exporter
- Example dataset generation

### Remaining

- Documentation
- CHANGELOG
- ADRs
- GitHub Actions
- Release

---

## 🔜 v0.3.0 — Lexicon

Build the tokenizer stack.

### Planned

- Byte-level tokenizer
- Vocabulary builder
- BPE tokenizer
- Save/load vocabulary
- Tokenizer benchmarks

---

## 🔜 v0.4.0 — Forge

Build the training pipeline.

### Planned

- Dataset loader
- Batch generation
- Training loop
- Optimizers
- Learning-rate schedulers
- Checkpointing

---

## 🔜 v0.5.0 — Transformer

Implement a modern decoder-only transformer.

### Planned

- Embeddings
- Multi-head attention
- Feed-forward networks
- Positional encodings
- KV cache
- Text generation

---

## 🔜 v0.6.0 — Inference

Focus on efficient inference.

### Planned

- Sampling strategies
- Streaming generation
- Model loading
- Performance improvements

---

## 🔜 v0.7.0 — Agents

Introduce agent capabilities.

### Planned

- Tool calling
- Memory
- Planning
- Reflection
- Multi-step reasoning

---

## 🎯 v1.0.0 — NanoForge

A complete educational AI engineering framework.

Goals:

- End-to-end LLM pipeline
- Production-inspired architecture
- Extensive documentation
- Educational examples
- Stable public API

---

# Future Ideas

Ideas that are intentionally out of scope for the current milestone.

- Distributed training
- Quantization
- Vision models
- Multimodal datasets
- Reinforcement learning
- Mixture of Experts
- GUI Playground

These ideas will only be considered after the core roadmap has been completed.

---

# Current Focus

Current milestone:

**v0.2.0 — Foundations**

Current objective:

Finish the documentation and developer experience before moving to tokenization.