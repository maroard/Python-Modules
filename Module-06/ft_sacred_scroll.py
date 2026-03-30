import alchemy

def main():
    print()
    print("=== Sacred Scroll Mastery ===")

    print()
    print("Testing direct module access:")
    try:
        print("alchemy.elements.create_fire(): "
              f"{alchemy.elements.create_fire()}")
        print("alchemy.elements.create_water(): "
              f"{alchemy.elements.create_water()}")
        print("alchemy.elements.create_earth(): "
              f"{alchemy.elements.create_earth()}")
        print("alchemy.elements.create_air(): "
              f"{alchemy.elements.create_air()}")
    except AttributeError as error:
        print(f"Error: {error}")

    print()
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.create_water(): {alchemy.create_water()}")
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as error:
        print(f"Error: {error}")

    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
