# Data Processor Hierarchy

> Sources: Code Nexus subject document, 2026-11-07
> Raw: [source](../../raw/code-nexus/code-nexus-abstract-architecture.md)
> Updated: 2026-11-07

## Overview

The foundation of the Code Nexus data plane is an abstract processor hierarchy. An abstract `DataProcessor` (inheriting from `ABC`) defines a common interface through two abstract methods, `validate` and `ingest`, plus a concrete `output` method. Three specialized processors — `NumericProcessor`, `TextProcessor`, and `LogProcessor` — override the abstract methods to handle different data kinds while sharing the same extraction contract.

## Abstract Interface

- `validate(self, data: Any) -> bool`: checks whether the supplied data can be ingested by this processor. The signature stays `Any` in every override because the processor cannot know in advance what will be sent.
- `ingest(self, data: Any) -> None`: processes and stores the input. Overrides declare their own specific accepted types. If invalid data is ingested without prior validation, an exception must be raised.
- `output(self) -> tuple[int, str]`: extracts the oldest stored piece of data together with its processing rank, removing it from the processor. Not overridden in specialized classes.

## Specialized Processors

- **NumericProcessor**: ingests `int`, `float`, and lists of both (including mixed-type lists). Converts data into strings and stores each item separately. Ingest signature reflects the accepted types.
- **TextProcessor**: ingests `str` and lists of strings. Stores data internally, one item per entry.
- **LogProcessor**: ingests a dict of string key-value pairs, and lists of that type. Converts data into strings and stores each item separately.

## Output Contract

`output` returns a `(rank, value)` tuple where `rank` is the processing rank within the processor and `value` is the oldest stored piece, which is then removed. This makes each processor a FIFO queue of processed items.

## Validation and Error Behavior

Each processor's `validate` returns `True` only for data it can handle. Calling `ingest` on invalid data without prior validation raises an exception such as `Improper numeric data`. This intentional misuse produces a mypy warning by design.

## See Also

- [Data Stream and Pipeline](data-stream-and-pipeline.md)
