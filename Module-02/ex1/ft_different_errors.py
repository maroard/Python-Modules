def garden_operations():
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError as error:
        print(f"Caught ValueError: {error}\n")
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}\n")
    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}\n")
    try:
        print("Testing KeyError...")
        plants = {
            "tomatos": 5,
            "carrots": 10
        }
        plants["missing_plant"]
    except KeyError as error:
        print(f"Caught KeyError: {error}\n")
    try:
        print("Testing multiple errors together...")
        open("missing.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
