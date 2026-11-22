#!/usr/bin/env python3


from ex3 import TransformFactory, has_transform_capability


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformFactory()
    base = factory.create_base()
    print("base:")
    print(base)
    print(base.attack())
    if has_transform_capability(base):
        print(base.transform())
    print(base.attack())
    if has_transform_capability(base):
        print(base.revert())
    print("evolved:")
    evolved = factory.create_evolved()
    print(evolved)
    print(evolved.attack())
    if has_transform_capability(evolved):
        print(evolved.transform())
    print(evolved.attack())
    if has_transform_capability(evolved):
        print(evolved.revert())


if __name__ == "__main__":
    main()
