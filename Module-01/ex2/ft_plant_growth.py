class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def aging(self) -> None:
        self.age += 1

    def get_info(self) -> str:
        return "Growth this week: 6cm"


def main() -> None:
    print("=== Garden Plant Growth ===")

    plants = [Plant("Rose", 25, 30)]
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        for plant in plants:
            plant.show()
            plant.grow()
            plant.aging()
    for plant in plants:
        print(plant.get_info())


if __name__ == "__main__":
    main()
