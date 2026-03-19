class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def __str__(self):
        return (f"{self.name} (Flower): "
                f"{self.height}cm, {self.age} days, "
                f"{self.color} color")

    def bloom(self):
        return (f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def __str__(self):
        return (f"{self.name} (Tree): "
                f"{self.height}cm, {self.age} days, "
                f"{self.trunk_diameter}cm diameter")

    def produce_shade(self):
        return (f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def __str__(self):
        return (f"{self.name} (Vegetable): "
                f"{self.height}cm, {self.age} days, "
                f"{self.harvest_season} harvest")

    def get_nutritional_value(self):
        return (f"{self.name} is {self.nutritional_value}")


def main() -> None:
    print("=== Garden Plant Types ===")

    plants = [Flower("Rose", 25, 30, "red"),
              Flower("Sunflower", 80, 45, "yellow"),
              Tree("Oak", 500, 1025, 50),
              Tree("Maple", 300, 900, 40),
              Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C"),
              Vegetable("Carrot", 30, 70, "autumn", "rich in vitamin A")]
    for plant in plants:
        if isinstance(plant, Flower):
            print(f"\n{plant}")
            print(plant.bloom())
        if isinstance(plant, Tree):
            print(f"\n{plant}")
            print(plant.produce_shade())
        if isinstance(plant, Vegetable):
            print(f"\n{plant}")
            print(plant.get_nutritional_value())


if __name__ == "__main__":
    main()
