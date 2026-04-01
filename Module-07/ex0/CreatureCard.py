from Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack > 0 and health > 0:
            self.attack = attack
            self.health = health
        else:
            raise ValueError("Attack and Health must be positive integers!")

    def play(self, game_stats: dict = {}) -> dict:
        if game_stats == {}:
            game_stats = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }

        return game_stats

    def attack_target(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": True if self.attack >= target.health else False
        }

    def get_card_info(self):
        card_info = super().get_card_info()
        card_info["type"] = "Creature"
        card_info["attack"] = self.attack
        card_info["health"] = self.health

        return card_info
