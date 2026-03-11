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
                if plant is None or plant == "":
                    raise PlantError("Plant name cannot be empty!")
                else:
                    self.plants.append(plant)
                    print(f"Added {plant} successfully")
            except PlantError as error:
                print(f"Error adding plant: {error}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                try:
                    if plant is None or plant == "":
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
            if plant_name is None or plant_name == "":
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
                print(f"{plant_name}: healthy (water: {water_level}"
                      f", sun: {sunlight_hours})")
        except PlantError as error:
            print(f"Error checking {plant_name}: {error}")

    @staticmethod
    def check_water_level(water_level: int):
        min_threshold = 1
        if water_level < min_threshold:
            raise WaterError("Not enough water in tank")


def test_garden_management():
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plants(["tomato", "lettuce", None])

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant_health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 7)

    print("\nTesting error recovery...")
    try:
        manager.check_water_level(0)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    finally:
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")
    test_garden_management()
