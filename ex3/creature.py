from abc import ABC, abstractmethod
from typing import TypeGuard


class Creature(ABC):
    _name: str
    _type: str

    def __init__(self, name: str, creature_type: str):
        self._name = name
        self._type = creature_type

    def __str__(self) -> str:
        return f"{self._name} is a {self._type} type Creature"

    def describe(self) -> str:
        return str(self)

    @abstractmethod
    def attack(self) -> str:
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


def has_transform_capability(obj: Creature) -> TypeGuard[TransformCapability]:
    return isinstance(obj, TransformCapability)


class Shiftling(Creature, TransformCapability):
    _transformed: bool

    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} performs a boosted strike"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    _transformed: bool

    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return f"{self._name} unleashes a devastating morph strike!"
        return f"{self._name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self._name} stablizes its form."


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:  # ruff: ignore[no-self-use]
        return Flameling()

    def create_evolved(self) -> Creature:  # ruff: ignore[no-self-use]
        return Pyrodon()


class TransformFactory(CreatureFactory):
    def create_base(self) -> Creature:  # ruff: ignore[no-self-use]
        return Shiftling()

    def create_evolved(self) -> Creature:  # ruff: ignore[no-self-use]
        return Morphagon()
