# Entity Factories and Capabilities

> Sources: Code Nexus subject document, 2026-11-07
> Raw: [source](../../raw/code-nexus/code-nexus-abstract-architecture.md)
> Updated: 2026-11-07

## Overview

The combat sandbox introduces two answers to questions the data hierarchy left open: who creates objects (abstract factory), and how to bolt an ability onto a type without corrupting its family tree (capability as a separate abstract class). Entities live in the `ex3/` package, which exposes only factories, never concrete entities.

## Creature Hierarchy

- `Creature` (ABC): holds `name` and `type` attributes; abstract method `attack`; concrete method `describe` returning a standard message built from name and type.
- Concrete entities inheriting from `Creature`:
  - `Flameling` (Fire type): attack returns `Flameling uses Ember!`
  - `Pyrodon` (Fire/Flying type): attack returns `Pyrodon uses Flamethrower!`

## TransformCapability

`TransformCapability` is an ABC defining abstract methods `transform` and `revert`. It must not inherit from `Creature`: an ability should not be forced onto every entity. An attribute tracks the transformed state and changes what `attack` returns.

Concrete entities inheriting from both `Creature` and `TransformCapability`:

- `Shiftling` (Normal type): attacks normally; transformed attack is a boosted strike.
- `Morphagon` (Normal/Dragon type): attacks normally; transformed attack is a devastating morph strike.

## CreatureFactory

`CreatureFactory` (ABC) declares `create_base` and `create_evolved`. Concrete factories:

- `FlameFactory`: base `Flameling`, evolved `Pyrodon`.
- `TransformCreatureFactory`: base `Shiftling`, evolved `Morphagon`.

## Package Exposure

The `ex3` package must expose only the factories, never the concrete entities. Concrete classes remain internal implementation details.

## Why a Capability Is Not a Creature

Putting `transform` and `revert` on the `Creature` base class would force every entity to carry transform state and methods, even plain entities like `Flameling`. That corrupts the family tree: plain entities would need no-op or invalid implementations, and the hierarchy would no longer reflect which entities can actually transform.

## See Also

- [Abstract Strategy Tournament](abstract-strategy-tournament.md)
