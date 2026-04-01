from abc import ABC, abstractmethod
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    UNCOMMON = "Uncommon"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENNDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        rarities = [r.value for r in Rarity]
        if rarity.capitalize() not in rarities:
            self.rarity = "Common"
        else:
            self.rarity = rarity

    @abstractmethod
    def play(self, game_stats: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
