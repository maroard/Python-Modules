from abc import ABC, abstractmethod
from ex0.Card import Card
from typing import Dict


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list[Card]) -> Dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict:
        pass

    @abstractmethod
    def get_magic_stats(self) -> Dict:
        pass
