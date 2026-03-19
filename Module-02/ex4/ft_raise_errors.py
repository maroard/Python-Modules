def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None:
        raise ValueError("Plant name cannot be empty!")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high ",
                         "(max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks():
    print("Testing good values...")
    check_plant_health("tomato", 3, 8)

    try:
        print("Testing empty plant name...")
        check_plant_health(None, 8, 4)
    except ValueError as error:
        print(f"Error: {error}\n")

    try:
        print("Testing bad water level...")
        check_plant_health("carrot", 15, 7)
    except ValueError as error:
        print(f"Error: {error}\n")

    try:
        print("Testing bad sunlight hours...")
        check_plant_health("lettuce", 3, 0)
    except ValueError as error:
        print(f"Error: {error}\n")

    print("All error raising tests completed!")


def main() -> None:
    print("=== Garden Plant Health Checker ===\n")

    test_plant_checks()


if __name__ == "__main__":
    main()
