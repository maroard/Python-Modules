import sys
import importlib


def main() -> None:
    if sys.prefix == sys.base_prefix:
        print("You must execute this program in a virtual environment!")
        return

    print()
    print("LOADING STATUS: Loading programs...")

    print()
    print("Checking dependencies:")

    pandas = None
    numpy = None
    pyplot = None

    try:
        pandas = importlib.import_module("pandas")
        print(f"[OK] pandas ({pandas.__version__}) "
              "- Data manipulation ready")
    except ModuleNotFoundError:
        print("[KO] pandas - Missing dependency")

    try:
        numpy = importlib.import_module("numpy")
        print(f"[OK] numpy ({numpy.__version__}) "
              "- Numerical computation ready")
    except ModuleNotFoundError:
        print("[KO] numpy - Missing dependency")

    try:
        matplotlib = importlib.import_module("matplotlib")
        pyplot = importlib.import_module("matplotlib.pyplot")
        print(f"[OK] matplotlib ({matplotlib.__version__}) "
              "- Visualization ready")
    except ModuleNotFoundError:
        print("[KO] matplotlib - Missing dependency")

    if pandas is None or numpy is None or pyplot is None:
        print()
        print("Missing required dependencies.")
        print("Install them with pip:\n"
              "pip install -r requirements.txt")
        print("Or with Poetry:\n"
              "poetry install")
        return

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    x = numpy.arange(1000)
    signal = numpy.sin(x / 50)
    noise = numpy.random.normal(0, 0.2, 1000)
    y = signal + noise

    data = pandas.DataFrame({
        "step": x,
        "signal": y
    })

    print("Generating visualization...")

    pyplot.figure(figsize=(10, 5))
    pyplot.plot(data["step"], data["signal"])
    pyplot.title("Matrix Signal Analysis")
    pyplot.xlabel("Step")
    pyplot.ylabel("Signal Strength")
    pyplot.savefig("matrix_analysis.png")
    pyplot.close()

    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
