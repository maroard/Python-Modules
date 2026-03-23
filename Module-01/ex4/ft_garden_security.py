class Plant:
    def __init__(self, name, height, age):
        self.name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            print("Using default height: 0cm")
            self._height = 0
        else:
            self._height = round(height, 1)

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            print("Using default age: 0 days")
            self._age = 0
        else:
            self._age = age

    def show(self):
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = round(value, 1)
        print(f"Height updated: {value}cm")

    def get_height(self):
        return self._height

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = value
        print(f"Age updated: {value} days")

    def get_age(self):
        return self._age


def main():
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    plant.show()
    print("")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-5)
    plant.set_age(-1)
    print("")
    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()
