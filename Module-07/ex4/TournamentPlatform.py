from ex4.TournamentCard import TournamentCard
from typing import Dict, List
import random


class TournamentPlatform():
    def __init__(self):
        self.participants = []
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.participants.append(card)

        interfaces = []
        for base in card.__class__.__bases__:
            interfaces.append(base.__name__)

        interfaces_label = ", ".join(interfaces)

        return (
            f"{card.name} (ID: {card.id}):\n"
            f"- Interfaces: [{interfaces_label}]\n"
            f"- Rating: {card.rating}\n"
            f"- Record: {card.record['wins']}-{card.record['losses']}"
        )

    def create_match(self, card1_id: str, card2_id: str) -> Dict:
        card1: TournamentCard = None
        card2: TournamentCard = None

        for card in self.participants:
            if card.get_card_info()["id"] == card1_id:
                card1 = card
            elif card.get_card_info()["id"] == card2_id:
                card2 = card

        starting_card: TournamentCard = random.choice([card1, card2])
        finishing_card: TournamentCard = (card2 if starting_card == card1
                                          else card1)

        while 1:
            incoming_attack = starting_card.attack(finishing_card)
            defense_info = finishing_card.defend(incoming_attack["damage"])
            if not defense_info["still_alive"]:
                winner = starting_card
                winner.update_wins(1)

                loser = finishing_card
                loser.update_losses(1)

                break

            incoming_attack = finishing_card.attack(starting_card)
            defense_info = starting_card.defend(incoming_attack["damage"])
            if not defense_info["still_alive"]:
                winner = finishing_card
                winner.update_wins(1)

                loser = starting_card
                loser.update_losses(1)

                break

        winner.calculate_rating()
        loser.calculate_rating()

        self.matches_played += 1

        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> List[str]:
        leaderboard: List[str] = []

        i = 0
        for card in self.participants:
            leaderboard.append(
                f"{i + 1}. {card.name} "
                f"- Rating: {card.rating} "
                f"({card.record['wins']}-{card.record['losses']})"
            )
            i += 1

        return leaderboard

    def generate_tournament_report(self) -> Dict:
        avg_rating = (
            sum([card.rating for card in self.participants])
            / len(self.participants)
        )

        if len(self.participants) > 1:
            platform_status = "active"
        else:
            platform_status = "inactive"

        return {
            "total_cards": len(self.participants),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": platform_status
        }
