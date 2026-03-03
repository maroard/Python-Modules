class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return (f"{self.name} ({self.height}cm, {self.age} days)")

    def grow(self):
        self.height += 1

    def aging(self):
        self.age += 1

    def get_info(self):
        return "Growth this week: +6cm"


if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(f"Created: {plant}")
    print(f"\nTotal plants created: {len(plants)}")
