from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_sequence(target: str, power: int) -> list[str]:
        results = []

        for spell in spells:
            results.append(spell(target, power))

        return results

    return cast_sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} defense"

    def can_cast(target: str, power: int) -> bool:
        return power >= 10 and target != ""

    print()
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print()
    print("Testing power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print()
    print("Testing conditional caster...")
    safe_fireball = conditional_caster(can_cast, fireball)
    print(safe_fireball("Dragon", 12))
    print(safe_fireball("Dragon", 5))

    print()
    print("Testing spell sequence...")
    combo = spell_sequence([fireball, heal, shield])
    results = combo("Dragon", 15)
    for spell_result in results:
        print(spell_result)


if __name__ == "__main__":
    main()
