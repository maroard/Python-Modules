from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Dict
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Fire Dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        else:
            return CreatureCard("Goblin Warrior", 3, "Uncommon", 2, 3)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Lightning Bolt":
            return SpellCard("Lightning Bolt", 3, "Common", "Damage")
        else:
            return SpellCard("Fireball", 3, "Uncommon", "Damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "Mana Crystal":
            return ArtifactCard("Mana Crystal", 2, "Rare", 6,
                                "Permanent: +1 mana per turn")
        else:
            return ArtifactCard("Enchanted Shield", 3, "Uncommon", 5,
                                "Permanent: reduce incoming damage by 1")

    def create_themed_deck(self, size: int) -> Dict[Card]:
        creatures = ["Fire Dragon", "Goblin Warrior"]
        spells = ["Lightning Bolt", "Fireball"]
        artifacts = ["Mana Crystal", "Enchanted Shield"]

        cards_in_deck = []

        for _ in range(size):
            selected_type = random.choice(["Creature", "Spell", "Artifact"])

            if selected_type == "Creature":
                cards_in_deck.append(
                    self.create_creature(random.choice(creatures)))
            elif selected_type == "Spell":
                cards_in_deck.append(
                    self.create_spell(random.choice(spells)))
            else:
                cards_in_deck.append(
                    self.create_artifact(random.choice(artifacts)))

        return {
            "creatures": [card for card in cards_in_deck
                          if card.get_card_info()["type"] == "Creature"],
            "spells": [card for card in cards_in_deck
                       if card.get_card_info()["type"] == "Spell"],
            "artifacts": [card for card in cards_in_deck
                          if card.get_card_info()["type"] == "Artifact"],
            "total_cards": size
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["lightning_bolt", "fireball"],
            "artifacts": ["mana_crystal", "enchanted_shield"]
        }
