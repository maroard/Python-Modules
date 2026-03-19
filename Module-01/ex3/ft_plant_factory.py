class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return (f"{self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    print("=== Plant Factory Output ===")

    plants = [Plant("Rose", 25, 30),
              Plant("Oak", 200, 365),
              Plant("Cactus", 5, 90),
              Plant("Sunflower", 80, 45),
              Plant("Fern", 15, 120)]
    for plant in plants:
        print(f"Created: {plant}")

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
