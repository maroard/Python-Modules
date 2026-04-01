import alchemy


def main() -> None:
    print()
    print("=== Sacred Scroll Mastery ===")

    print()
    print("Testing direct module access:")
    try:
        print("alchemy.elements.create_fire(): ", end="")
        print(alchemy.elements.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.elements.create_water(): ", end="")
        print(alchemy.elements.create_water())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.elements.create_earth(): ", end="")
        print(alchemy.elements.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.elements.create_air(): ", end="")
        print(alchemy.elements.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print()
    print("Testing package-level access (controlled by __init__.py):")
    try:
        print("alchemy.create_fire(): ", end="")
        print(alchemy.create_fire())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_water(): ", end="")
        print(alchemy.create_water())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        print(alchemy.create_earth())
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")

    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
