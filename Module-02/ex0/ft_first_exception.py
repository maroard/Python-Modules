def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
    else:
        print(f"Temperature {temp}°C is perfect for plants!\n")


def test_temperature_input():
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")

    test_temperature_input()


if __name__ == "__main__":
    main()
