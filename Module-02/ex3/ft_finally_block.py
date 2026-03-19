def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            else:
                print(f"Watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")
    try:
        print("Testing with error...")
        water_plants(["tomato", None])
    finally:
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")

    test_watering_system()


if __name__ == "__main__":
    main()
