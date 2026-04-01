from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard
from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print()
    print("=== DataDeck Ability System ===")

    print()
    print("EliteCard capabilities:")
    for cls in [Card, Combatable, Magical]:
        print(f"- {cls.__name__}: {[name for name in dir(cls)
              if not name.startswith("__")
              and callable(getattr(cls, name))]}")

    print()
    print("Playing Arcane Warrior (Elite Card):")

    elite_card = EliteCard("Arcane Warrior", 7, "Legendary",
                           5, 10, "melee", 3,
                           {"Fireball": 4})
    enemy = CreatureCard("Enemy", 4, "Epic", 5, 6)

    print()
    print("Combat phase:")
    print(f"Attack result: {elite_card.attack(enemy)}")
    print("Defense result: "
          f"{elite_card.defend(enemy.get_card_info()["attack"])}")

    enemy_1 = CreatureCard("Enemy1", 2, "Common", 1, 3)
    enemy_2 = CreatureCard("Enemy2", 3, "Uncommon", 2, 3)

    print()
    print("Magic phase:")
    print(f"Spell cast: {elite_card.cast_spell("Fireball",
                                               [enemy_1, enemy_2])}")
    print(f"Mana channel: {elite_card.channel_mana(3)}")

    print()
    print("Multiple interface implementation successful!")
