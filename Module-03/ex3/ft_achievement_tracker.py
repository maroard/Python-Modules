import random


def gen_player_achievements() -> set[str]:
    all_achievements = [
        "First Steps",
        "Boss Slayer",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Strategist",
        "World Savior",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "Sharp Mind",
        "Unstoppable",
        "Crafting Genius",
        "Hidden Path Finder",
    ]

    count = random.randint(5, 9)
    return set(random.sample(all_achievements, count))


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    print()
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    print()
    all_distinct = set()
    for achievements in players.values():
        all_distinct = all_distinct | achievements
    print(f"All distinct achievements: {all_distinct}")

    print()
    common_achievements = None
    for achievements in players.values():
        if common_achievements is None:
            common_achievements = achievements
        else:
            common_achievements = common_achievements & achievements
    print(f"Common achievements: {common_achievements}")

    print()
    for name, achievements in players.items():
        others_union = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others_union = others_union | other_achievements
        print(f"Only {name} has: {achievements - others_union}")

    print()
    for name, achievements in players.items():
        print(f"{name} is missing: {all_distinct - achievements}")


if __name__ == "__main__":
    main()
