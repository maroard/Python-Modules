def main() -> None:
    print()
    print("=== Pathway Debate Mastery ===")

    print()
    print("Testing Absolute Imports (from basic.py):")
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("lead_to_gold(): ", end="")
    print(lead_to_gold())
    print("stone_to_gem(): ", end="")
    print(stone_to_gem())

    print()
    print("Testing Relative Imports (from advanced.py):")
    from alchemy.transmutation.advanced import (philosophers_stone,
                                                elixir_of_life)
    print("philosophers_stone(): ", end="")
    print(philosophers_stone())
    print("elixir_of_life(): ", end="")
    print(elixir_of_life())

    print()
    print("Testing Package Access:")
    import alchemy
    print("alchemy.transmutation.lead_to_gold(): ", end="")
    print(alchemy.transmutation.lead_to_gold())
    print("alchemy.transmutation.philosophers_stone(): ", end="")
    print(alchemy.transmutation.philosophers_stone())

    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
