from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
from typing import Dict


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_dmg: int, health: int, combat_type: str, armor: int,
                 card_id: str, rating: int):
        super().__init__(name, cost, rarity)

        self.attack_dmg = attack_dmg
        self.health = health
        self.combat_type = combat_type
        self.armor = armor

        self.id = card_id
        self.rating = rating
        self.record = {"wins": 0, "losses": 0}

    def play(self, game_state: Dict = {}) -> Dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "TournamentCard summoned to arena"
        }

    def attack(self, target: Card) -> Dict:
        return {
            "attacker": self.name,
            "target": target.get_card_info()["name"],
            "damage": self.attack_dmg,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> Dict:
        if incoming_damage > self.armor:
            self.health += self.armor - incoming_damage

        return {
            "defender": self.name,
            "damage_taken": 0 if self.armor >= incoming_damage
            else incoming_damage - self.armor,
            "damage_blocked": self.armor if incoming_damage >= self.armor
            else incoming_damage,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> Dict:
        return {
            "attack_dmg": self.attack_dmg,
            "health": self.health,
            "armor": self.armor,
            "combat_type": self.combat_type
        }

    def update_wins(self, wins: int) -> None:
        self.record["wins"] += wins

    def update_losses(self, losses: int) -> None:
        self.record["losses"] += losses

    def calculate_rating(self) -> int:
        self.rating += self.record["wins"] * 16 - self.record["losses"] * 16

        return self.rating

    def get_rank_info(self) -> Dict:
        ranks = ["Novice", "Brave", "Elite", "Champion", "Arena Legend"]

        if self.rating < 1200:
            rank = ranks[0]
        elif self.rating >= 1200 and self.rating < 2000:
            rank = ranks[1]
        elif self.rating >= 2000 and self.rating < 3000:
            rank = ranks[2]
        elif self.rating >= 3000 and self.rating < 5000:
            rank = ranks[3]
        else:
            rank = ranks[4]

        return {
            "rank": rank,
            "rating": self.rating
        }

    def get_tournament_stats(self) -> Dict:
        return {
            "id": self.id,
            "elo_gain": self.record["wins"] * 16 - self.record["losses"] * 16,
            "wins": self.record["wins"],
            "losses": self.record["losses"]
        }

    def get_card_info(self) -> Dict:
        card_info = super().get_card_info()
        card_info["type"] = "Tournament Card"
        card_info.update(self.get_combat_stats())
        card_info.update(self.get_rank_info())
        card_info.update(self.get_tournament_stats())

        return card_info
