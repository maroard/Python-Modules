class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return (f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    plants = [Plant("Rose", 25, 30),
              Plant("Sunflower", 80, 45),
              Plant("Cactus", 15, 120)]
    for plant in plants:
        print(plant)
