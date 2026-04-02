from ex0.CreatureCard import CreatureCard
from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard


if __name__ == "__main__":
    print()
    print("=== DataDeck Deck Builder ===")

    print()
    print("Building deck with different card types...")
    deck = Deck([])
    cards = [CreatureCard("Fire Dragon", 5, "Legendary", 7, 5),
             ArtifactCard("Mana Crystal", 2, "Rare", 6,
                          "Permanent: +1 mana per turn"),
             SpellCard("Lightning Bolt", 3, "Common", "Damage")]

    for card in cards:
        deck.add_card(card)

    print(deck.get_deck_stats())

    print()
    print("Drawing and playing cards:")

    while deck.cards:
        print()
        card = deck.draw_card()
        card_info = card.get_card_info()

        print(f"Drew: {card_info["name"]} ({card_info["type"]})")
        print(f"Play result: {card.play()}")

    print()
    print("Polymorphism in action: Same interface, different card behaviors")
