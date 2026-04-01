from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name, cost, rarity, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_stats: dict = {}):
        if game_stats == {}:
            game_stats = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Permanent: +1 mana per turn"
            }

        return game_stats

    def activate_ability(self):
        pass
