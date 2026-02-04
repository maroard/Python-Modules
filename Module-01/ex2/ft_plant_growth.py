class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def display_infos(self):
        print("{}:".format(self.name), end=" ")
        print("{}cm,".format(self.height), end=" ")
        print("{} days old".format(self.age))
    def grow(self):
        self.height += 1
    def aging(self):
        self.age += 1
    def get_info(self):
        return "Growth this week: +6cm"

if __name__ == "__main__":
    plants = [Plant("Rose", 25, 30)]
    print("=== Day 1 ===")
    for plant in plants:
        plant.display_infos()
    for i in range(6):
        for plant in plants:
            plant.grow()
            plant.aging()
    print("=== Day 7 ===")
    for plant in plants:
        plant.display_infos()
    print(plants[0].get_info())
