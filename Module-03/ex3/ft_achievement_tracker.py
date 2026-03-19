def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon",
               "perfectionist"}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print("\n=== Achievement Analytics ===")

    achievements = alice.union(bob).union(charlie)
    print(f"All unique achievements: {achievements}")
    print(f"Total unique achievements: {len(achievements)}\n")

    common_achievements = alice.intersection(bob).intersection(charlie)
    rare_achievements = set()
    for achievement in achievements:
        occurrence = 0
        for player in [alice, bob, charlie]:
            if achievement in player:
                occurrence += 1
        if occurrence == 1:
            rare_achievements.add(achievement)
    print(f"Common to all players: {common_achievements}")
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
