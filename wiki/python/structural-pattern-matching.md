# Structural Pattern Matching in Python

> Sources: Real Python (Bartosz Zaczyński), Updated Oct 16, 2024
> Raw: [source](../../raw/python/realpython-structural-pattern-matching.md)
> Updated: 2026-11-09

## Overview

Structural pattern matching is a control flow construct introduced in Python 3.10. It compares a *subject* expression against *patterns* in `case` clauses and runs the first matching block. Patterns can match by type, shape, value, and identity, and can destructure (bind) parts of the subject to names. It combines conditional branching with object deconstruction in a declarative style.

## Syntax and Semantics

- `match <subject>:` starts a block that may contain only `case` clauses.
- `case <pattern> [if <guard>]:` matches when the pattern succeeds and the optional guard evaluates truthy.
- Patterns are evaluated top to bottom; at most one `case` runs (no C-style fallthrough). Overlapping patterns make order important; place specific cases before general ones.
- A wildcard pattern (`case _:`) is commonly used as a default catch-all. `match`, `case`, and `_` are soft keywords in the pattern-matching context.
- `match` is a statement (not an expression). Cases are not required to be exhaustive.
- Assignment expressions (Walrus operator) cannot be used inside `case` clauses; use capture patterns or `as` aliases to bind matched values.

## Pattern Types

- **Literal/value patterns**: match fixed values (with nuances: most literals compare by equality; `True`, `False`, and `None` match by identity in literal patterns).
- **Capture patterns**: bind a matched value to a name (each capture name must be unique within a pattern; union alternatives must bind the same set of names).
- **Sequence patterns**: match ordered sequences and can unpack elements; strings/bytes/bytearrays are treated as scalar values, not sequence patterns.
- **Mapping patterns**: match mappings by key structure.
- **Class patterns**: match instances by type and destructure via positional/keyword patterns (behavior can be customized with `__match_args__`).
- **OR patterns (`|`)**: match any of several alternatives.
- **AS patterns**: bind an alias to a matched (sub)pattern.
- **Guards**: `if` conditions evaluated after a structural match succeeds.

## Practical Uses and Caveats

Useful for decisions based on the structure of complex/hierarchical data and simultaneous destructuring (e.g., nested mappings/sequences, parsing/dispatch by shape). Less suited to complex, non-exclusive business-rule chains where `if/elif` may be clearer.

Caveats highlighted by the source include: floating-point literal matching can be imprecise due to representation; matching constants by bare name creates a capture pattern (use dotted/qualified names or guards); Python sets have no dedicated set pattern syntax (use class patterns/guards or value checks); captured names may remain undefined if no matching case binds them.

## See Also

- [Inheritance and Composition in Python](../python-oop/inheritance-and-composition.md)
