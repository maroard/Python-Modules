class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def is_tomato_plant_watered(water_level: int):
    min_threshold = 3
    if water_level < min_threshold:
        raise PlantError("The tomato plant is wilting!")


def is_water_tank_empty(water_level: int):
    min_threshold = 1
    if water_level < min_threshold:
        raise WaterError("Not enough water in the tank!")


def check_plants_health():
    try:
        print("Testing PlantError...")
        is_tomato_plant_watered(2)
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")
    try:
        print("Testing WaterError...")
        is_water_tank_empty(0)
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")
    print("Testing catching all garden errors...")
    try:
        is_tomato_plant_watered(2)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        is_water_tank_empty(0)
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    check_plants_health()
