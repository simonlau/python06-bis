#!/usr/bin/env python3


from ex3 import CreatureFactory, FlameFactory, TransformFactory


def info(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(f"{base}")
    print(f"{base.attack()}")
    print(f"{evolved}")
    print(f"{evolved.attack()}")


def fight(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    one = factory1.create_base()
    two = factory2.create_base()

    print(one)
    print("vs.")
    print(two)
    print("fight!")
    print(one.attack())
    print(two.attack())


def main() -> None:
    print("Testing factory")
    info(FlameFactory())
    print()
    print("Testing factory")
    info(TransformFactory())
    print()
    print("Testing battle")
    fight(FlameFactory(), TransformFactory())


if __name__ == "__main__":
    main()
