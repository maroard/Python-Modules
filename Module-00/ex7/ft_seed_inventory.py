def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (seed_type == "tomato"):
        seed_type = "Tomato seeds:"
    elif (seed_type == "carrot"):
        seed_type = "Carrot seeds:"
    elif (seed_type == "lettuce"):
        seed_type = "Lettuce seeds:"
    if (unit == "packets"):
        print(seed_type, quantity, "packets available")
    elif (unit == "grams"):
        print(seed_type, quantity, "grams total")
    elif (unit == "area"):
        print(seed_type, "covers", quantity, "square meters")
    else:
        print("Unknown unit type")
