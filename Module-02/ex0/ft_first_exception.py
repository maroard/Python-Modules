def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("Input data is '25'")
    try:
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("Input data is 'abc'")
    try:
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")

    test_temperature()


if __name__ == "__main__":
    main()
