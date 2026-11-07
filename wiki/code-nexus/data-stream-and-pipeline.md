# Data Stream and Pipeline

> Sources: Code Nexus subject document, 2026-11-07
> Raw: [source](../../raw/code-nexus/code-nexus-abstract-architecture.md)
> Updated: 2026-11-07

## Overview

`DataStream` routes a mixed-type stream to registered processors using polymorphic behavior, then exports consumed results through a duck-typed plugin system. It builds on the data processor hierarchy and demonstrates both subtype polymorphism (routing by `validate`) and structural typing (export plugins).

## DataStream

- `register_processor(self, proc: DataProcessor) -> None`: registers a processor to handle stream elements.
- `process_stream(self, stream: list[Any]) -> None`: analyzes each element and sends it to the first registered processor whose `validate` returns `True`; prints an error when no processor can handle an element.
- `print_processors_stats(self) -> None`: prints per-processor totals and remaining counts.

Routing relies on each processor's `validate` method, so `DataStream` never needs to know concrete processor types.

## ExportPlugin Protocol

A new `ExportPlugin` class inherits from the special `Protocol` class and defines:

- `process_output(self, data: list[tuple[int, str]]) -> None`: constraint for each export plugin. The `data` type matches the return of `DataProcessor.output`.

Plugins are made export-compatible through duck typing rather than inheritance.

## Output Pipeline

`DataStream.output_pipeline(self, nb: int, plugin: ExportPlugin) -> None` is used after `process_stream`. It consumes `nb` elements from every registered processor and exports them through the provided plugin.

At least two plugins are required:

- **CSV export plugin**: emits comma-joined values per processor.
- **JSON export plugin**: emits an object keyed `item_<rank>` mapped to string values.

## ABC vs Protocol

`DataProcessor` is an ABC and `ExportPlugin` is a Protocol. Both constrain what a class must provide, but an ABC enforces through inheritance while a Protocol enforces through structural shape. A plugin system wants the Protocol because exporters need not inherit from a shared base — they only need to behave correctly.

## See Also

- [Data Processor Hierarchy](data-processor-hierarchy.md)
