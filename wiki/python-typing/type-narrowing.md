# Type Narrowing

> Sources: Python typing documentation, typing.python.org; Adam Johnson, 2021-06-09
> Raw: [source](../../raw/typing/typing-narrowing.md); [Adam Johnson: TypeGuard](../../raw/python-typing/adamj-typeguard-narrow-types.md)
> Updated: 2026-11-09

## Overview

*Type narrowing* is when a symbol has multiple possible types in a scope and a runtime conditional check refines it to a more specific type for type checkers. Commonly understood checks include `if x is not None`, truthiness checks, `isinstance(...)`, and `callable(...)`. Type checkers may also narrow instance attributes and sequence members (behavior varies by checker). The exact narrowing constructs supported are not specified and differ across type checkers.

## User-Defined Narrowing: `TypeIs` and `TypeGuard`

The type system provides `typing.TypeIs` and `typing.TypeGuard` to define custom narrowing functions (useful for reusable or checker-unrecognized checks). Both take an argument and return a boolean; they are used in `if` checks like `isinstance()`.

- `TypeIs[T]`: function returns `True` if and only if the argument is of type `T`. A `TypeIs` must be correct (return `True` for all members of `T` and `False` otherwise); type checkers cannot detect incorrect implementations, which can cause unsound checking.
- `TypeGuard[T]`: similar usage but different narrowing semantics; useful when narrowing to a type not assignable to the input, or when the function is not true for all members of the narrowed type.

Availability noted by the source: `TypeIs` in `typing` from Python 3.13 and in `typing_extensions` from version 4.10.0; `TypeGuard` in `typing` from Python 3.10 and in `typing_extensions` from version 3.10.0.0.

## `TypeIs` vs `TypeGuard` Semantics

- **Assignability**: `TypeIs` requires the narrowed type to be assignable to the input type; `TypeGuard` does not.
- **On `True`**: `TypeGuard` narrows to exactly the guard type; `TypeIs` can infer a more precise type combining prior knowledge with the `TypeIs` type (an “intersection type”).
- **On `False`**: `TypeGuard` cannot narrow; `TypeIs` can narrow to exclude the `TypeIs` type.

Prefer `TypeIs` when its constraints fit (often more intuitive and safer for narrowing). Use `TypeGuard` for non-assignable narrowing (e.g., `list[object]` to `list[int]`) or partial predicates, but avoid unsound narrowing across incompatible/invariant types (prefer covariant immutable parameter types like `Sequence`/`Iterable`).

## Safety and Soundness

Narrowing can be unsafe with mutability or dynamic behavior:

- `isinstance()`/`issubclass()` involve `__instancecheck__`/`__subclasscheck__` and may not be fully captured (e.g., `abc.ABC.register()`, runtime-checkable protocols have limits).
- Incorrect `TypeIs`/`TypeGuard` implementations are not validated by checkers; review and test them.
- `TypeGuard` can enable unsound narrowing with invariant mutable containers.
- **Invalidated assumptions**: conditions established earlier may be invalidated by later code (other threads/coroutines/calls), even for local variables in some cases; avoid narrowing on objects mutated elsewhere.

## See Also

- [TypedDict](typeddict.md)
- [Structural Pattern Matching in Python](../python/structural-pattern-matching.md)
