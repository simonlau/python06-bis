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
    tmp: list[tuple[Creature, BattleStrategy]] = []
    for factory, strategy in opponents:
        tmp.extend(
            [
                (factory.create_base(), strategy),
                (factory.create_evolved(), strategy),
            ]
        )
    y = itertools.combinations(tmp, 2)
    for i, (one, two) in enumerate(y):
        f1, s1 = one
        f2, s2 = two
        is_ok = s1.is_valid(f1) and s2.is_valid(f2)
        print(f"Tournament {i} ({'basic' if is_ok else 'error'})")
        print(f"[ ({f1!r}+{s1!r}), ({f2!r}+{s2!r}) ]")
        print("*** Tournament ***")
        print("2 opponents involved")
        print()
        print(" * Battle *")
        print(f1)
        print("vs.")
        print(f2)
        print("now fight!")
        if s1.is_valid(f1):
            s1.act(f1)
        else:
            print("Battle error, aborting tournament: ", end="")
            print(f"Invalid Creature '{f1!r}' ", end="")
            print("for this aggressive strategy")
            break
        if s2.is_valid(f2):
            s2.act(f2)
        else:
            print("Battle error, aborting tournament: ", end="")
            print(f"Invalid Creature '{f2!r}' ", end="")
            print("for this aggressive strategy")
            break
        print()


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
