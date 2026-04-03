from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AgressiveStrategy import AgressiveStrategy


if __name__ == "__main__":
    print()
    print("=== DataDeck Game Engine ===")

    print()
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.get_factory_name()}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Availabale types: {factory.get_supported_types()}")

    print()
    print("Simulating agressive turn...")

    hand = []
    for card in engine.hand:
        card_info = card.get_card_info()
        hand.append(f"{card_info['name']} ({card_info['cost']})")

    print(f"Hand: {hand}")

    print()
    print("Turn execution:")
    print(f"Strategy: {engine.strategy.get_strategy_name()}")
    print(f"Actions: {engine.simulate_turn()}")

    print()
    print("Game Report:")
    print(engine.get_engine_status())

    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
