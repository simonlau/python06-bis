# Python type hints: narrow types with `TypeGuard`

> Source: https://adamj.eu/tech/2021/06/09/python-type-hints-how-to-narrow-types-with-typeguard/
> Collected: 2026-11-09
> Published: 2021-06-09

I previously covered [type narrowing using `isinstance()`, `assert`, and `Literal`](/tech/2021/05/17/python-type-hints-how-to-narrow-types-with-isinstance-assert-literal/). In today’s post we’ll cover `TypeGuard`, a new special type that allows us to create custom type narrowing functions.

`TypeGuard` was defined in [PEP 647](https://www.python.org/dev/peps/pep-0647/), and is available on Python 3.10+, or on older versions from [`typing-extensions`](https://pypi.org/project/typing-extensions/). Guido van Rossum added support to Mypy in version 0.900, [which was released yesterday](https://mypy-lang.blogspot.com/2021/06/mypy-0900-released.html).

Recall that type narrowing uses particular expressions to infer that, in a given block, a variable has a more limited type than its definition. For example, using `isinstance()`:

```python
from __future__ import annotations

name: str | None

if isinstance(name, str):
    # name must be 'str'
    ...
else:
    # name must be None
    ...
```

Type checkers, including Mypy, support a limited number of expressions, such as `if isinstance(...)`. But the number of potentially type-narrowing expressions is infinite, especially for parameterized types such as containers. `TypeGuard` allows us to write type *any* expression and communicate to our type checker that it narrows types.

A type narrowing function is one that accepts at least one argument and returns a `bool`. Instead of marking the return type as `bool`, we use `TypeGuard[T]`, where `True` means the first argument has type `T`, and `False` means it does not. Take this example, adapted from the PEP:

```python
from __future__ import annotations

from typing_extensions import TypeGuard


def is_str_list(value: list[object]) -> TypeGuard[list[str]]:
    """Are all list items strings?"""
    return all(isinstance(x, str) for x in value)


x: list[object]

reveal_type(x)
if is_str_list(x):
    reveal_type(x)
```

`is_str_list()` returns `True` if the given list contains only strings. We tell Mypy this can narrow the type of `value` to `list[str]` with the `TypeGuard` return type.

Running Mypy on this file, we see this output from the [`reveal_type()` calls](/tech/2021/05/14/python-type-hints-how-to-debug-types-with-reveal-type/):

```
$ mypy --strict example.py
example.py:13: note: Revealed type is "builtins.list[builtins.object]"
example.py:15: note: Revealed type is "builtins.list[builtins.str]"
```

The second note shows us that within the `if` block, Mypy knows `x` must be a list of strings. This allows us to use the list items as `str`s there without any errors. Great!

`TypeGuard` is flexible as it allows us to write arbitrary code to narrow expressions. It does force us to move even short expressions into separate functions, but that can often a good thing for our code’s readability.

Because there are infinite possible expressions, type checkers cannot validate that our expressions line up with the guarded types. So we need to write our `TypeGuard` functions with care, and test them thoroughly.

PEP 647 also shows generic `TypeGuard` functions with `TypeVar`, but when I tried out the examples, I found Mypy 0.901 does not yet support them. There are a [few open issues for `TypeGuard`](https://github.com/python/mypy/issues?q=typeguard+is%3Aissue+is%3Aopen+) so it seems Mypy could use our contributions here!
