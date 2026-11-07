# Abstract Strategy Tournament

> Sources: Code Nexus subject document, 2026-11-07
> Raw: [source](../../raw/code-nexus/code-nexus-abstract-architecture.md)
> Updated: 2026-11-07

## Overview

The abstract strategy pattern lets entities from different families fight in a tournament without battle code that is aware of each capability. A `BattleStrategy` decides how an entity acts, checked via `isinstance` against capabilities rather than concrete families. This lives in the `ex4/` package, which imports factories from `ex3`.

## BattleStrategy

`BattleStrategy` (ABC) defines:

- `act`: called by the tournament to make an entity act.
- `is_valid`: returns a bool indicating whether an entity is suitable for the strategy.

If `act` is called with an unsuitable entity, a dedicated exception with a clear message is raised.

## Concrete Strategies

- **NormalStrategy**: suitable for any entity; simply calls `attack`.
- **AggressiveStrategy**: suitable only for entities with the transform capability; transforms, attacks, then reverts.

Capability checks use `isinstance`, never concrete family classes. Additional strategies may be added as long as one plain and one capability-aware strategy exist.

## Tournament

`tournament.py` creates entity factories from `ex3` and the strategies, then defines a single battle function that:

1. Takes a list of opponents, each a tuple of `(CreatureFactory, BattleStrategy)`.
2. Makes each opponent face every other once.
3. Applies each entity's strategy.
4. Aborts on an invalid entity-strategy pair.

## Where the Decision Moved

The decision of how an entity fights moved from the entity's family (and from capability-aware battle code) into the strategy object. Adding a new capability no longer requires editing battle code; a new strategy encapsulates the new behavior, and existing entities keep working unchanged.

## See Also

- [Entity Factories and Capabilities](entity-factories-and-capabilities.md)
