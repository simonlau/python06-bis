# TypedDict

> Sources: Mouse Vs Python (Mike Driscoll), 2025-06-17
> Raw: [source](../../raw/python-typing/mousevspython-typeddict.md)
> Updated: 2026-11-09

## Overview

`TypedDict` is a typing construct for adding type hints to *heterogeneous dictionaries* — dictionaries whose values are not all the same type. Python does not enforce type hints at runtime; external tools such as Mypy perform checking. `TypedDict` was introduced in Python 3.8 (PEP 589).

## Regular Dictionary Hints vs TypedDict

- A regular dict can be hinted as `dict[key_type, value_type]` (e.g., `dict[str, str]`). Before Python 3.9, `Dict` is imported from `typing`.
- For a dict with mixed value types (e.g., `list`, `str`, `int`), a broad union like `dict[str, list | str | int]` may work depending on checker configuration, but can be imprecise (e.g., operations on a list value may be hard for checkers to validate).
- A `TypedDict` defines the expected keys and the type of each value, giving checkers a precise shape.

## Defining a TypedDict

**Class-based form** (when keys are valid identifiers):

```python
from typing import TypedDict


class MultiTypeDict(TypedDict):
    names: list
    otype: str
    code: int
```

**Functional/constructor form** (supports keys with spaces or other non-identifier names): call `TypedDict(typename, fields_dict)` where `fields_dict` maps key names to types.

```python
Results = TypedDict(
    "Results",
    {
        "Animal Habitats": list,
        "Tested": bool,
        "Animal Name": str,
        "Animal Location": str,
    },
)
```

## Use Cases

Useful for complex dictionary shapes, including when such dicts appear inside lists, tuples, or other dictionaries. It can make type-hinting these structures clearer and help prevent hard-to-detect defects.

## See Also

- [Type Narrowing](type-narrowing.md)
