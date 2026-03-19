import sys
import math


def main() -> None:
    print("=== Game Coordinate System ===\n")

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("No or too much coordinates provided. Usage:"
              " python3 ft_coordinates_system.py <x,y,z>")

    else:
        try:

            coords = sys.argv[1].split(",")
            if len(coords) < 3 or len(coords) > 3:
                raise IndexError
            x = int(coords[0])
            y = int(coords[1])
            z = int(coords[2])
            position = (x, y, z)
            print(f"Parsing coordinates: \"{sys.argv[1]}\"")
            print(f"Parsed position: {position}")
            distance = math.sqrt((x - 0)**2 + (y - 0)**2 + (z - 0)**2)
            print(f"Distance between (0, 0, 0) and {position}: {distance}\n")

            print("Unpacking demonstration:")
            print(f"Player at x={x}, y={y}, z={z}")
            X, Y, Z = position
            print(f"Coordinates: X={X}, Y={Y}, Z={Z}")

        except ValueError as error:
            print(f"Parsing invalid coordinates: \"{sys.argv[1]}\"\n"
                  f"Error parsing coordinates: {error}\n"
                  f"Error details - Type: ValueError, Args: (\"{error}\",)")

        except IndexError:
            print(f"Error: {len(coords)} coordinate(s) given, but 3 needed"
                  " (x, y, z)")


if __name__ == "__main__":
    main()
