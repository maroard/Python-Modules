from ex0.CreatureCard import CreatureCard


if __name__ == "__main__":
    print()
    print("=== Datadeck Card Foundation ===")

    print()
    print("Testing Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print()
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print()
    print(f"Playing {fire_dragon.name} with 6 mana available:")
    is_playable = fire_dragon.is_playable(6)
    print(f"Playable: {is_playable}")
    if is_playable:
        print(f"Play result: {fire_dragon.play()}")

    goblin_warrior = CreatureCard("Goblin Warrior", 3, "Uncommon", 2, 3)

    print()
    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print()
    print("Testing insufficient mana (3 available):")
    is_playable = fire_dragon.is_playable(3)
    print(f"Playable: {is_playable}")

    print()
    print("Abstract pattern successfully demonstrated!")
