from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from typing import List, Dict


class AgressiveStrategy(GameStrategy):
    def execute_turn(self, hand: List[Card], battlefield: List[Card]) -> Dict:
        cards_to_play = [card for card in hand
                         if card.get_card_info()["type"] != 'Artifact']
        while len(cards_to_play) > 2:
            most_expensive_card = [card for card in cards_to_play
                                   if card.get_card_info()["cost"]
                                   == max([card.get_card_info()["cost"]
                                           for card in cards_to_play])][0]
            cards_to_play.remove(most_expensive_card)

        for card in cards_to_play:
            card.play(None)

        valid_targets = [target for target in battlefield
                         if target.get_card_info()["type"] != "Spell"]

        damage_dealt = 0
        if valid_targets:
            targets = self.prioritize_targets(valid_targets)

            targets_attacked = []
            last_target_attacked = None
            i = 0
            for card in cards_to_play:
                card_info = card.get_card_info()
                target_info = targets[i].get_card_info()
                if card_info["type"] == "Creature":
                    card.attack_target(targets[i])
                    damage_dealt += card_info["attack"]
                else:
                    card.resolve_effect([targets[i]])
                    damage_dealt += 3
                if targets[i] != last_target_attacked:
                    targets_attacked.append(targets[i])
                last_target_attacked = targets[i]
                if target_info["type"] == "Creature":
                    if targets[i].health <= 0:
                        if i == len(targets) - 1:
                            break
                        i += 1
                elif targets[i].durability <= 0:
                    if i == len(targets) - 1:
                        break
                    i += 1
        else:
            for card in cards_to_play:
                card_info = card.get_card_info()

                if card_info["type"] == "Creature":
                    damage_dealt += card_info["attack"]
                else:
                    damage_dealt += 3

        return {
            "cards_played": [card.get_card_info()["name"]
                             for card in cards_to_play],
            "mana_used": sum([card.get_card_info()["cost"]
                              for card in cards_to_play]),
            "targets_attacked": [target.get_card_info()["name"]
                                 for target in targets_attacked] if battlefield
            else ["Enemy Player"],
            "damage_dealt": damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: List[Card]) -> List:
        prioritized_targets = []
        targets = available_targets

        while len(prioritized_targets) < len(targets):
            weakest_target = (
                [target for target in targets
                 if target.get_card_info()
                 ["health" if target.get_card_info()["type"]
                  == "Creature" else "durability"]
                 == min([target.get_card_info()
                         ["health" if target.get_card_info()["type"]
                          == "Creature" else "durability"]
                         for target in targets])][0]
            )
            targets.remove(weakest_target)
            prioritized_targets.append(weakest_target)

        return prioritized_targets
