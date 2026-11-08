# Inheritance and Composition in Python

> Sources: Real Python (Isaac Rodriguez), Updated Oct 30, 2026
> Raw: [source](../../raw/python-oop/realpython-inheritance-composition-python.md)
> Updated: 2026-11-08

## Overview

Inheritance and composition model relationships between classes and enable code reuse in different ways. Inheritance models an **is a** relationship: a derived class extends a base class's interface and implementation. Composition models a **has a** relationship: a class contains objects of other classes (components) to build complex behavior. Both support reuse; composition often creates fewer dependencies.

## Inheritance

- A derived class inherits a base class's interface and implementation. In Python, classes implicitly derive from `object` (custom exceptions should derive from `BaseException`/`Exception`).
- **Liskov substitution principle**: if `S` is a subtype of `T`, replacing `T` objects with `S` objects should not change program behavior. A practical test: justify both "`B` is an `A`" and "`A` is a `B`"; if both hold, avoid inheriting between them (e.g., `Square`/`Rectangle` resizing exposes interface mismatch).
- **Abstract base classes**: Python's `abc` module (`ABC`, `@abstractmethod`) defines classes meant to be inherited, not instantiated; abstract methods must be overridden by concrete subclasses.
- **Implementation vs interface inheritance**: inheritance reuses implementation; Python's duck typing allows reuse when an object provides the required interface without inheriting a specific base.
- **Multiple inheritance**: Python supports inheriting from multiple base classes; MRO (method resolution order) determines initialization/method lookup and can cause subtle errors (e.g., incompatible `__init__` signatures in diamond-like hierarchies).
- **Mixins**: classes that provide reusable behavior to other classes without being treated as a base "is a" type; useful for cross-cutting features (e.g., dictionary serialization).

## Composition

- Composition combines objects of other types: a composite **has a** component. It reuses implementation by delegation rather than inheritance.
- **Policy-based design**: compose objects from interchangeable policy/strategy objects (roles, payroll policies, etc.) and delegate work to them. Policies can be swapped to change behavior, including at runtime (e.g., applying a long-term disability policy that wraps a base payroll policy).
- Construction complexity can be managed with factory methods or module-level singletons/public interfaces.

## Choosing Between Them

- Prefer inheritance to model a clear **is a** relationship and to reuse/extend a base implementation; verify with Liskov substitution.
- Prefer composition to model **has a** relationships, reuse components across unrelated classes, group interchangeable behaviors/policies, and enable runtime behavior changes with looser coupling.

## See Also

- [Data Processor Hierarchy](../code-nexus/data-processor-hierarchy.md)
- [Abstract Strategy Tournament](../code-nexus/abstract-strategy-tournament.md)
