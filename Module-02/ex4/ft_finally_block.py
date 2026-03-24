class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("Testing valid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("Testing invalid plants...")
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")

    test_watering_system()


if __name__ == "__main__":
    main()
