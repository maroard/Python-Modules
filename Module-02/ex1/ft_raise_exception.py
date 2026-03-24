def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)

    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature() -> None:
    test_values = ["25", "abc", "100", "-50"]

    for temp_str in test_values:
        print(f"Testing temperature: {temp_str}")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature {temp}°C is perfect for plants!\n")
        except ValueError as error:
            print(f"Error: {error}\n")

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
