from abc import ABC, abstractmethod

from ex3.creature import Creature, TransformCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, entity: Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def __repr__(self) -> str:
        return "Normal"

    # ruff: ignore[no-self-use]
    def act(self, entity: Creature) -> None:
        print(entity.attack())

    # ruff: ignore[no-self-use, unused-method-argument]
    def is_valid(self, entity: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def __repr__(self) -> str:
        return "Aggressive"

    # ruff: ignore[no-self-use]
    def act(self, entity: Creature) -> None:
        if isinstance(entity, TransformCapability):
            print(entity.transform())
            print(entity.attack())
            print(entity.revert())

    # ruff: ignore[no-self-use]
    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, TransformCapability)
