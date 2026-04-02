from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1.Deck import Deck
from typing import Dict


class GameEngine():
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

        datadeck = factory.create_themed_deck(20)
        self.deck = Deck(datadeck["creatures"]
                         + datadeck["spells"]
                         + datadeck["artifacts"])

        self.hand = []
        for _ in range(5):
            self.hand.append(self.deck.draw_card())

        self.battlefield = []
        for _ in range(0):
            self.battlefield.append(self.deck.draw_card())

        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = datadeck["total_cards"]

    def simulate_turn(self) -> Dict:
        turn_summary = self.strategy.execute_turn(self.hand,
                                                  self.battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_summary["damage_dealt"]

        return turn_summary

    def get_engine_status(self) -> Dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
