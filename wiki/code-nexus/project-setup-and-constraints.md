# Project Setup and Constraints

> Sources: Code Nexus subject document, 2026-11-07
> Raw: [source](../../raw/code-nexus/code-nexus-abstract-architecture.md)
> Updated: 2026-11-07

## Overview

General constraints and repository layout for the Code Nexus project. Exercises 0–2 are single files at the repository root, each improving on the previous; exercises 3 and 4 are packages requiring an `__init__.py`.

## Language and Quality

- Python 3.10 or later.
- flake8 coding standard.
- Comprehensive type annotations, checked with mypy.
- Exception handling must protect data streams from corruption.

## Authorized Imports

Only `abc` and `typing` (plus standard builtins and standard collections/methods). External libraries are forbidden. `eval()` and `exec()` are forbidden.

## Repository Layout

```
.
|-- data_processor.py
|-- data_stream.py
|-- data_pipeline.py
|-- ex3
|   |-- __init__.py
|   `-- (all files needed by the exercise)
|-- battle.py
|-- capacitor.py
|-- ex4
|   |-- __init__.py
|   `-- (all files needed by the exercise)
`-- tournament.py
```

## Packaging Prerequisite

Exercises 3 and 4 are packages importing each other. Familiarity with `__init__.py` and what a package exposes is required; each package must have an `__init__.py`.

## Evaluation Notes

During defense, explanations of polymorphic behavior, method overriding, and extension with new data types, entity families, or strategies may be requested. Only requested files need to be submitted.

## See Also

- [Data Processor Hierarchy](data-processor-hierarchy.md)
- [Data Stream and Pipeline](data-stream-and-pipeline.md)
- [Entity Factories and Capabilities](entity-factories-and-capabilities.md)
- [Abstract Strategy Tournament](abstract-strategy-tournament.md)
