from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


if __name__ == "__main__":
    print()
    print("=== Datadeck Tournament Platform ===")

    tournament = TournamentPlatform()

    card1 = TournamentCard("Fire Dragon", 5, "Legendary",
                           7, 12, "melee", 2,
                           "dragon_001", 1200)
    card2 = TournamentCard("Ice Wizard", 4, "Epic",
                           5, 10, "magic", 3,
                           "wizard_001", 1150)

    print()
    print("Registering Tournament Cards...")

    print()
    print(tournament.register_card(card1))

    print()
    print(tournament.register_card(card2))

    print()
    print("Creating tournament match...")
    print(f"Match result: {tournament.create_match(card1.id, card2.id)}")

    print()
    print("Tournament Leaderboard:")
    for element in tournament.get_leaderboard():
        print(element)

    print()
    print("Platform Report:")
    print(tournament.generate_tournament_report())

    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
