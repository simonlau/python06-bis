from abc import ABC, abstractmethod


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
    def transform(self) -> None:
        pass

    @abstractmethod
    def revert(self) -> None:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")

    def attack(self) -> str:
        return f"{self._name} attacks normally."

    def transform(self) -> None:
        pass

    def revert(self) -> None:
        pass


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        return f"{self._name} attacks normally."

    def transform(self) -> None:
        pass

    def revert(self) -> None:
        pass


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
