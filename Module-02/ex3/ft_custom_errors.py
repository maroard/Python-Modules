class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(water_level: int) -> None:
    if water_level < 3:
        raise PlantError("The tomato plant is wilting!")


def check_water_tank(water_level: int) -> None:
    if water_level < 1:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    try:
        print("Testing PlantError...")
        check_plant_health(2)
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    try:
        print("Testing WaterError...")
        check_water_tank(0)
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant_health(2)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    try:
        check_water_tank(0)
    except GardenError as error:
        print(f"Caught a garden error: {error}")

    print("\nAll custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    test_custom_errors()


if __name__ == "__main__":
    main()
