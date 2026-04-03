from ex0.Card import Card
from typing import Dict


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict = {}) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> Dict:
        if self.durability > 0:
            self.durability -= 1

        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability": self.durability,
            "success": self.durability > 0
        }

    def get_card_info(self) -> Dict:
        card_info = super().get_card_info()
        card_info["type"] = "Artifact"
        card_info["durability"] = self.durability
        card_info["effect"] = self.effect

        return card_info
