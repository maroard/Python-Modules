from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_dmg: int, health: int, combat_type: str, armor: int,
                 spells: dict[str, int]):
        super().__init__(name, cost, rarity)
        self.attack_dmg = attack_dmg
        self.health = health
        self.combat_type = combat_type
        self.armor = armor
        self.spells = spells
        self.mana = 8

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "EliteCard summoned to battlefield"
        }

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.get_card_info()["name"],
            "damage": self.attack_dmg,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
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

    def get_combat_stats(self) -> dict:
        return {
            "attack_dmg": self.attack_dmg,
            "health": self.health,
            "armor": self.armor,
            "combat_type": self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list[Card]) -> dict:
        if spell_name in self.spells:
            has_enough_mana = self.spells[spell_name] <= self.mana
            if has_enough_mana:
                mana_used = self.spells[spell_name]
                self.mana -= mana_used
                spell_label = f"{spell_name}"
            else:
                mana_used = 0
                spell_label = f"{spell_name} (insufficient mana)"
        else:
            mana_used = 0
            spell_label = f"{spell_name} (unknown spell)"
        return {
            "caster": self.name,
            "spell": spell_label,
            "targets": [target.get_card_info()["name"] for target in targets],
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_remaining": self.mana,
            "spells": self.spells
        }

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = "Elite Card"
        card_info.update(self.get_combat_stats())
        card_info.update(self.get_magic_stats())

        return card_info
