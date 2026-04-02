from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AgressiveStrategy import AgressiveStrategy


if __name__ == "__main__":
    print()
    print("=== DataDeck Game Engine ===")

    print()
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()

    print(f"Factory: {FantasyCardFactory.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    # print(f"Availabale types: {}")

    print()
    print("Simulating agressive turn...")
    # print(f"Hand: {}")
