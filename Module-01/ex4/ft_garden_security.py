class SecurePlant:
    def __init__(self, name):
        self.name = name
        self._height = 0
        self._age = 0

    def __str__(self):
        return (f"{self.name} ({self._height}cm, {self._age} days)")

    def set_height(self, value):
        if (value < 0):
            print(f"\nInvalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
            return
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def get_height(self):
        return self._height

    def set_age(self, value):
        if (value < 0):
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]")

    def get_age(self):
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plants = [SecurePlant("Rose")]
    print(f"Plant created: {plants[0].name}")
    plants[0].set_height(25)
    plants[0].set_age(30)
    plants[0].set_height(-5)
    plants[0].get_height()
    print(f"Current plant: {plants[0]}")
