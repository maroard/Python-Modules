import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_inp = input("Enter new coordinates as floats in format 'x,y,z': ")
        coords = user_inp.split(",")

        if len(coords) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(coords[0])
            y = float(coords[1])
            z = float(coords[2])
            return (x, y, z)
        except ValueError:
            for coord in coords:
                try:
                    float(coord)
                except ValueError as error:
                    print(f"Error on parameter '{coord}': {error}")
                    break


def main() -> None:
    print("=== Game Coordinate System ===")

    print()
    print("Get a first set of coordinates")
    first_pos = get_player_pos()
    print(f"Got a first tuple: {first_pos}")

    x, y, z = first_pos
    print(f"It includes: X={x}, Y={y}, Z={z}")

    distance_center = math.sqrt((x - 0)**2 + (y - 0)**2 + (z - 0)**2)
    print(f"Distance to center: {round(distance_center, 4)}")

    print()
    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance_between = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance_between, 4)}")


if __name__ == "__main__":
    main()
