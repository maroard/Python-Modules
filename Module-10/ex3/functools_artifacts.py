from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(add, spells)
    if operation == "multiply":
        return reduce(mul, spells)
    if operation == "max":
        return reduce(max, spells)
    if operation == "min":
        return reduce(min, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchantment": partial(base_enchantment, 50, "fire"),
        "water_enchantment": partial(base_enchantment, 50, "water"),
        "earth_enchantment": partial(base_enchantment, 50, "earth")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(value: Any) -> str:
        return "Unknown spell type"

    @spell.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @spell.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @spell.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return spell


def main() -> None:
    def base_enchantment(power: int, element: str, target: str) -> str:
        return (f"{element.capitalize()} enchantment on {target} "
                f"with {power} power")

    print()
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")

    print()
    print("Testing partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    print(enchantments["fire_enchantment"]("Sword"))
    print(enchantments["water_enchantment"]("Shield"))
    print(enchantments["earth_enchantment"]("Armor"))

    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print()
    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["heal", "shield", "blink"]))
    print(dispatcher(3.14))


if __name__ == "__main__":
    main()
