from enum import Enum
from ex0.Card import Card


class EffectType(Enum):
    DAMAGE = "Damage"
    HEAL = "Heal"
    BUFF = "Buff"
    DEBUFF = "Debuff"


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        effect_types = [type.value for type in EffectType]
        if effect_type.capitalize() not in effect_types:
            self.effect_type = "Damage"
        else:
            self.effect_type = effect_type

    def play(self, game_stats: dict) -> dict:
        pass

    def resolve_effect(self, targets: list) -> dict:
        pass
