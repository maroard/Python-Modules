import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        elif arg.count(":") != 1:
            print("Error - invalid parameter")
            continue

        item, quantity_str = arg.split(":")

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory.update({item: quantity})

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    for item, quantity in inventory.items():
        percentage = round(quantity / total_quantity * 100, 1)
        print(f"Item {item} represents {percentage}%")

    most_abundant_item = None
    most_abundant_qty = None
    least_abundant_item = None
    least_abundant_qty = None

    for item, quantity in inventory.items():
        if most_abundant_qty is None or quantity > most_abundant_qty:
            most_abundant_item = item
            most_abundant_qty = quantity

        if least_abundant_qty is None or quantity < least_abundant_qty:
            least_abundant_item = item
            least_abundant_qty = quantity

    print(f"Item most abundant: {most_abundant_item} with quantity "
          f"{most_abundant_qty}")
    print(f"Item least abundant: {least_abundant_item} with quantity "
          f"{least_abundant_qty}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
