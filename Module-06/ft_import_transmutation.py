def main() -> None:
    print()
    print("=== Import Transmutation Mastery ===")

    print()
    print("Method 1 - Full module import:")
    import alchemy
    print("alchemy.elements.create_fire(): ", end="")
    print(alchemy.elements.create_fire())

    print()
    print("Method 2 - Specific function import: ")
    from alchemy.elements import create_water
    print("create_water(): ", end="")
    print(create_water())

    print()
    print("Method 3 - Aliased import:")
    from alchemy.potions import healing_potion as heal
    print("heal(): ", end="")
    print(heal())

    print()
    print("Method 4 - Multiple imports:")
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strenght_potion
    print("create_earth(): ", end="")
    print(create_earth())
    print("create_fire(): ", end="")
    print(create_fire())
    print("strenght_potion(): ", end="")
    print(strenght_potion())

    print()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
