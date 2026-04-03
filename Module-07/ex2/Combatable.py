from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: Card) -> Dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> Dict:
        pass
