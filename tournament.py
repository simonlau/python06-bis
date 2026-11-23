#!/usr/bin/env python3

import itertools
from typing import TypeAlias

from ex3 import CreatureFactory, FlameFactory, TransformFactory
from ex3.creature import Creature
from ex4.strategy import AggressiveStrategy, BattleStrategy, NormalStrategy

Opponent: TypeAlias = tuple[CreatureFactory, BattleStrategy]


def create_creatures(
    factory: CreatureFactory, strategy: BattleStrategy
) -> tuple[tuple[Creature, BattleStrategy], tuple[Creature, BattleStrategy]]:
    return (
        (factory.create_base(), strategy),
        (factory.create_evolved(), strategy),
    )


def battle(opponents: list[Opponent]) -> None:
    x = []
    for factory, strategy in opponents:
        # ruff: ignore[repeated-append]
        x.append((factory.create_base(), strategy))
        x.append((factory.create_evolved(), strategy))
    y = itertools.combinations(x, 2)
    for i, (one, two) in enumerate(y):
        f1, s1 = one
        f2, s2 = two
        print(f"Tournament {i} (???)")
        print(f"[ ({f1!r}+{s1!r}), ({f2!r}+{s2!r}) ]")
        print("*** Tournament ***")
        print("2 opponents involved")
        print()
        print(" * Battle *")
        print(f1)
        print("vs.")
        print(f2)
        print("now fight!")
        s1.act(f1)
        s2.act(f2)


def main() -> None:
    opponents: list[Opponent] = [
        (FlameFactory(), NormalStrategy()),
        (FlameFactory(), AggressiveStrategy()),
        (TransformFactory(), NormalStrategy()),
        (TransformFactory(), AggressiveStrategy()),
    ]
    battle(opponents)


if __name__ == "__main__":
    main()
