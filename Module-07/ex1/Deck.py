from ex0.Card import Card
from typing import List, Dict
from random import shuffle


class Deck():
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.total_cards = len(cards)
        self.creatures_count = 0
        self.spells_count = 0
        self.artifacts_count = 0

        for card in cards:
            card_info = card.get_card_info()
            if card_info["type"] == "Creature":
                self.creatures_count += 1
            elif card_info["type"] == "Spell":
                self.spells_count += 1
            else:
                self.artifacts_count += 1

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        self.total_cards += 1

        card_info = card.get_card_info()
        if card_info["type"] == "Creature":
            self.creatures_count += 1
        elif card_info["type"] == "Spell":
            self.spells_count += 1
        else:
            self.artifacts_count += 1

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.get_card_info()["name"] == card_name:
                self.cards.remove(card)
                self.total_cards -= 1
                return True

        return False

    def shuffle(self) -> None:
        shuffle(self.cards)

    def draw_card(self) -> Card:
        drew_card = None

        try:
            drew_card = self.cards.pop()
            self.total_cards -= 1
        except IndexError:
            print("Deck can't be empty to draw a card!")

        return drew_card

    def get_deck_stats(self) -> Dict:
        avg_cost = round(sum(card.get_card_info()["cost"]
                             for card in self.cards) / self.total_cards, 1)

        return {
            "total_cards": self.total_cards,
            "creatures": self.creatures_count,
            "spells": self.spells_count,
            "artifacts": self.artifacts_count,
            "avg_cost": avg_cost
        }
