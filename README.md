# NanoForge

> **Build. Understand. Engineer.**

**NanoForge** is an educational AI engineering framework for building modern language models from first principles.

Instead of hiding complexity behind high-level libraries, NanoForge teaches how modern AI systems are engineered by implementing every major component from scratch with a strong focus on architecture, testing, and clean software design.

---

# Why NanoForge?

Most AI repositories teach you **how to use** a framework.

NanoForge teaches you **how to build one.**

The goal is to create a complete AI engineering framework covering every stage of the modern LLM pipeline:

- Dataset Generation
- Tokenization
- Vocabulary Building
- Training Pipeline
- Transformer Models
- Inference
- AI Agents

Every component is designed to be readable, well-tested, and educational.

---

# Current Features

## Dataset Pipeline

- ✅ Synthetic dataset generation
- ✅ Streaming dataset generator
- ✅ Deterministic entity generation
- ✅ Task registry
- ✅ Copy task
- ✅ Prompt templates
- ✅ JSONL exporter

## Engineering

- ✅ Modular architecture
- ✅ Unit-tested components
- ✅ Feature branch workflow
- ✅ Conventional commits
- ✅ Reproducible generation

---

# Project Roadmap

```
Datasets
    │
    ▼
Tokenizer
    │
    ▼
Vocabulary
    │
    ▼
Training
    │
    ▼
Transformer
    │
    ▼
Inference
    │
    ▼
Agents
```

Current milestone:

> **v0.2.0 — Foundations**

---

# Quick Start

Clone the repository.

```bash
git clone https://github.com/<your-username>/NanoForge.git

cd NanoForge
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install NanoForge.

```bash
pip install -e .
```

Generate your first dataset.

```bash
python examples/generate_copy_dataset.py
```

---

# Example Output

```
==================================================
NanoForge Dataset Generation
==================================================

Generated 100 samples

Saved to:

datasets/copy_dataset.jsonl

==================================================
```

---

# Project Structure

```
src/
└── nanoforge/
    ├── datasets/
    ├── tokenizer/
    ├── model/
    ├── trainer/
    ├── inference/
    ├── agent/
    ├── ui/
    └── utils/

examples/

tests/

docs/
```

---

# Engineering Principles

NanoForge follows a few core engineering principles.

- One class, one responsibility.
- Streaming over loading entire datasets into memory.
- Deterministic generation through explicit random seeds.
- Composition over inheritance.
- Readable code over clever code.
- Every feature includes automated tests.
- Every merge leaves `develop` green.

---

# Testing

Run the full test suite.

```bash
pytest
```

Current project status:

```
40 passing tests
```

---

# Contributing

NanoForge is built using a disciplined engineering workflow.

- Feature branches
- Pull request workflow
- Conventional commits
- Code reviews
- Automated testing

Contributions, discussions, and ideas are welcome.

---

# Roadmap

See:

```
ROADMAP.md
```

---

## 📄 License

NanoForge is released under the MIT License.

See the `LICENSE` file for details.

## Continuous Integration

Every push and pull request automatically runs the NanoForge test suite using GitHub Actions.

This ensures that the `develop` and `main` branches always remain stable.

## Example

Train a tokenizer from raw text:

```bash
python examples/train_tokenizer.py

```

## 📄 New Tests

Let's also test the public API rather than only examples.

Create:

```text
tests/
    test_examples.py
```
