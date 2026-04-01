from ex0.Card import Card
from typing import List


class Deck():
    def __init__(self, cards: List[Card]):
        self.cards = cards
        self.total_cards = len(cards)
        self.creatures = 0
        self.spells = 0
        self.artifacts = 0

        for card in cards:
            card_info = card.get_card_info()
            if card_info["type"] == "Creature":
                self.creatures += 1
            elif card_info["type"] == "Spell":
                self.spells += 1
            else:
                self.artifacts += 1

    def add_card(self, card: Card) -> None:
        pass

    def remove_card(self, card_name: str) -> None:
        pass

    def shuffle(self):
        pass

    def draw_card(self):
        pass

    def get_deck_stats(self):
        pass
