import sys
import os
import site


def main() -> None:
    if sys.prefix != sys.base_prefix:
        print()
        print("MATRIX STATUS: Welcome to the construct")

        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")

        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")

        print()
        print(f"Package installation path: {site.getsitepackages()[0]}")
    else:
        print()
        print("MATRIX STATUS: You're still plugged in")

        print()
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print()
        print("WARNING: You're in the global environment!")
        print("The machine can see everything you install.")

        print()
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows")

        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
