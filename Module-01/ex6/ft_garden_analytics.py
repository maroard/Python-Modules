class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1

    def __str__(self):
        return (f"{self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def __str__(self):
        return super().__str__() + f", {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, prize_points):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def __str__(self):
        return super().__str__() + f", Prize points: {self.prize_points}"


class GardenManager:
    def __init__(self, gardener, plants_collection):
        self.gardener = gardener
        self.plants_collection = plants_collection
        self.plants_added = 0
        self.total_growth = 0

    @classmethod
    def create_garden_network(cls, gardeners):
        gardens = []
        for gardener in gardeners:
            gardens.append(cls(gardener, plants_collection=[]))
        return (gardens)

    def add_plant(self, new_plant):
        self.plants_collection.append(new_plant)
        self.plants_added += 1
        print(f"Added {new_plant.name} to {self.gardener}'s garden")

    def grow_plants(self):
        print(f"\n{self.gardener} is helping all plants grow...")
        for plant in self.plants_collection:
            plant.grow()
            self.total_growth += 1
            print(f"{plant.name} grew 1cm")

    class GardenStats:
        @staticmethod
        def print_plants_collection(plants):
            print("Plants in garden:")
            for plant in plants:
                print(f"- {plant}")

        @staticmethod
        def print_stats(plants_added, total_growth, plants):
            regular_plants = 0
            flowering_plants = 0
            prize_flowers = 0
            print(f"\nPlants added: {plants_added}, "
                  f"Total Growth: {total_growth}cm")
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    prize_flowers += 1
                elif isinstance(plant, FloweringPlant):
                    flowering_plants += 1
                else:
                    regular_plants += 1
            print(f"Plant types: {regular_plants} regular, "
                  f"{flowering_plants} flowering, "
                  f"{prize_flowers} prize flowers")

    def print_report(self):
        print(f"\n=== {self.gardener}'s Garden Report ===")
        self.GardenStats.print_plants_collection(self.plants_collection)
        self.GardenStats.print_stats(self.plants_added, self.total_growth,
                                     self.plants_collection)

    @staticmethod
    def valid_height(height):
        if height < 0:
            return (False)
        return (True)


if __name__ == "__main__":
    gardens = GardenManager.create_garden_network(["Alice", "Bob"])
    plants_1 = [Plant("Oak", 100),
                FloweringPlant("Rose", 25, "red"),
                PrizeFlower("Sunflower", 50, "yellow", 10)]
    plants_2 = [Plant("Maple", 300)]
    print("=== Garden Management System Demo ===\n")
    for plant in plants_1:
        gardens[0].add_plant(plant)
    for plant in plants_2:
        gardens[1].add_plant(plant)
    for garden in gardens:
        for plant in garden.plants_collection:
            if not garden.valid_height(plant.height):
                valid_heights = False
                break
            else:
                valid_heights = True
    for garden in gardens:
        garden.grow_plants()
    for garden in gardens:
        garden.print_report()
    print(f"\nHeight validation test: {valid_heights}")
    garden_scores = []
    for garden in gardens:
        score = 0
        for plant in garden.plants_collection:
            score += plant.height
            if isinstance(plant, PrizeFlower):
                score += plant.prize_points
        garden_scores.append(score)
    print("Garden scores - ", end="")
    i = 0
    for garden in gardens:
        print(f"{garden.gardener}: {garden_scores[i]}", end=""
              + ", " if i < len(gardens) - 1 else "\n")
        i += 1
    print(f"Total gardens managed: {len(gardens)}")
