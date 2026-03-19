class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height += 1

    def aging(self):
        self.age += 1

    def get_info(self):
        return "Growth this week: +6cm"


def main() -> None:
    plants = [Plant("Rose", 25, 30)]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant)
    for i in range(6):
        for plant in plants:
            plant.grow()
            plant.aging()

    print("=== Day 7 ===")
    for plant in plants:
        print(plant)
    print(plants[0].get_info())


if __name__ == "__main__":
    main()
