def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda mage: mage["power"])["power"],
        "min_power": min(mages, key=lambda mage: mage["power"])["power"],
        "avg_power": round(sum(mage["power"] for mage in mages)
                           / len(mages), 2)
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ancient Scroll", "power": 40, "type": "knowledge"},
    ]

    mages = [
        {"name": "Aelric", "power": 78, "element": "fire"},
        {"name": "Lyra", "power": 95, "element": "ice"},
        {"name": "Tomas", "power": 61, "element": "earth"},
        {"name": "Mira", "power": 42, "element": "wind"},
    ]

    spells = ["fireball", "heal", "shield"]

    print()
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)")

    print()
    print("Testing power filter...")
    filtered_mages = power_filter(mages, 70)
    for mage in filtered_mages:
        print(f"{mage['name']} ({mage['power']} power)")

    print()
    print("Testing spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print()
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']}")
    print(f"Min power: {stats['min_power']}")
    print(f"Avg power: {stats['avg_power']}")


if __name__ == "__main__":
    main()
