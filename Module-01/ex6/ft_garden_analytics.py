class Plant:
    class _Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def show_stats(self):
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, "
                  f"{self.show_calls} show")

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant._Stats()

    def show(self):
        self._stats.show_calls += 1
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self):
        self._height = round(self._height + 8.0, 1)
        self._stats.grow_calls += 1

    def age(self):
        self._age += 1
        self._stats.age_calls += 1

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def display_stats(self):
        self._stats.show_stats()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def bloom(self):
        self.has_bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self):
            super().__init__()
            self.shade_calls = 0

        def show_stats(self):
            super().show_stats()
            print(f" {self.shade_calls} shade")

    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree._TreeStats()

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self):
        self._stats.shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age(self):
        super().age()
        self.nutritional_value += 1


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def bloom(self):
        super().bloom()
        self.seed_count = 42

    def show(self):
        super().show()
        print(f" Seeds: {self.seed_count}")


def display_plant_statistics(plant):
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)
    print("")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)
    print("")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    for _ in range(20):
        sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)
    print("")

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_statistics(unknown)
    print("")


if __name__ == "__main__":
    main()
