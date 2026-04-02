from enum import Enum
from ex0.Card import Card


class EffectType(Enum):
    DAMAGE = "Damage"
    HEAL = "Heal"
    BUFF = "Buff"
    DEBUFF = "Debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)

        effect_types = [e_type.value for e_type in EffectType]
        if effect_type.capitalize() not in effect_types:
            raise ValueError("effect_type must be "
                             "'Damage' / 'Heal' / 'Buff' / 'Debuff'")

        self.effect_type = effect_type.capitalize()
        if self.effect_type == "Damage":
            self.effect = "Deal 3 damage to target"
        elif self.effect_type == "Heal":
            self.effect = "Heal 2 HP to friendly target"
        elif self.effect_type == "Buff":
            self.effect = "Increase friendly target's Attack by 1"
        else:
            self.effect = "Decrease target's Attack by 1"

    def play(self, game_state: dict = {}) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def resolve_effect(self, targets: list[Card]) -> dict:
        spell_recap = {}
        spell_recap["targets"] = []
        spell_recap["effects"] = []

        for target in targets:
            target_info = target.get_card_info()

            target_name = target_info["name"]
            spell_recap["targets"].append(target_name)

            target_type = target_info["type"]
            if target_type == "Spell":
                spell_recap["effects"].append("You can't cast a Spell "
                                              "on another Spell!")
                continue

            if self.effect_type == "Damage":
                effect_label = f"Dealt 3 damage to {target_name}"

                if target_type == "Artifact":
                    target.durability -= 3
                    effect_label += " (durability)"
                else:
                    target.health -= 3

                spell_recap["effects"].append(effect_label)
            elif self.effect_type == "Heal":
                if target_type == "Artifact":
                    target.durability += 2
                    effect_label = f"Repaired 2 durability of {target_name}"
                else:
                    target.health += 2
                    effect_label = f"Healed 2 HP to {target_name}"

                spell_recap["effects"].append(effect_label)
            elif self.effect_type == "Buff":
                if target_type == "Artifact":
                    spell_recap["effects"].append("You can't apply a buff "
                                                  "to an Artifact!")
                else:
                    target.attack += 1
                    spell_recap["effects"].append(f"Increased {target_name}'s "
                                                  "Attack by 1")
            else:
                if target_type == "Artifact":
                    spell_recap["effects"].append("You can't apply a debuff "
                                                  "to an Artifact!")
                else:
                    target.attack -= 1
                    spell_recap["effects"].append(f"Decreased {target_name}'s "
                                                  "Attack by 1")

        return spell_recap

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = "Spell"
        card_info["effect_type"] = self.effect_type

        return card_info
