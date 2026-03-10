class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plants(self, new_plants):
        for plant in new_plants:
            try:
                if plant is None:
                    raise ValueError("Plant name cannot be empty!")
                else:
                    self.plants.append(plant)
                    print(f"Added {plant} successfully")
            except ValueError as error:
                print(f"Error adding plant: {error}\n")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                try:
                    if plant is None or not isinstance(plant, str):
                        raise WaterError(f"Cannot water {plant}"
                                         " - invalid plant!")
                    else:
                        print(f"Watering {plant} - success")
                except WaterError as error:
                    print(f"Error: {error}")
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant_name, water_level, sunlight_hours):
        try:
            if plant_name is None:
                raise PlantError("Plant name cannot be empty!")
            elif water_level > 10:
                raise PlantError(f"Water level {water_level} is too high"
                                 " (max 10)")
            elif water_level < 1:
                raise PlantError(f"Water level {water_level} is too low"
                                 " (min 1)")
            elif sunlight_hours > 12:
                raise PlantError(f"Sunlight hours {sunlight_hours} is too high"
                                 " (max 12)")
            elif sunlight_hours < 2:
                raise PlantError(f"Sunlight hours {sunlight_hours} is too low"
                                 " (min 2)")
            else:
                print(f"Plant '{plant_name}' is healthy!\n")
        except PlantError as error:
            print(f"Error checking {plant_name}: {error}\n")


def test_garden_management():
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plants(["tomato", "lettuce", None])

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant_health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 7)


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
