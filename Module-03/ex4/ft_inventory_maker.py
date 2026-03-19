import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print("No argument provided. Usage:"
              " python3 ft_inventory_system.py <item:quantity> ...")

    else:
        try:
            inventory = {}
            for arg in sys.argv[1:]:
                item, quantity = arg.split(":")
                inventory.update({item: int(quantity)})
            total_items = 0
            for value in inventory.values():
                total_items += value
            print(f"Total items in inventory: {total_items}")
            print(f"Unique item types: {len(inventory)}")

            print("\n=== Current Inventory ===")
            inventory_copy = dict(inventory)
            while inventory_copy:
                most_abundant_item = None
                most_abundant_qty = 0
                for item, quantity in inventory_copy.items():
                    if quantity > most_abundant_qty:
                        most_abundant_item = item
                        most_abundant_qty = quantity
                most_unit_label = "unit" if most_abundant_qty == 1 else "units"
                print(f"{most_abundant_item}:"
                      f" {most_abundant_qty} {most_unit_label}"
                      f" ({most_abundant_qty / total_items * 100:.1f}%)")
                del inventory_copy[most_abundant_item]

            print("\n=== Inventory Statistics ===")
            most_abundant_item = None
            most_abundant_qty = 0
            least_abundant_item = None
            least_abundant_qty = 0
            for item, quantity in inventory.items():
                if quantity > most_abundant_qty:
                    most_abundant_item = item
                    most_abundant_qty = quantity
                if quantity < least_abundant_qty or least_abundant_qty == 0:
                    least_abundant_item = item
                    least_abundant_qty = quantity
            most_unit_label = "unit" if most_abundant_qty == 1 else "units"
            least_unit_label = "unit" if least_abundant_qty == 1 else "units"
            print(f"Most abundant: {most_abundant_item}"
                  f" ({most_abundant_qty} {most_unit_label})")
            print(f"Least abundant: {least_abundant_item}"
                  f" ({least_abundant_qty} {least_unit_label})")

            print("\n=== Item Categories ===")
            moderate_items = {}
            scarce_items = {}
            for item, qty in inventory.items():
                if qty < 5:
                    scarce_items.update({item: qty})
                else:
                    moderate_items.update({item: qty})
            print(f"Moderate: {moderate_items}")
            print(f"Scarce: {scarce_items}")

            print("\n=== Management Suggestions ===")
            to_restock = ""
            count = 0
            restock_count = 0
            for item, qty in inventory.items():
                if qty == least_abundant_qty:
                    restock_count += 1
            for item, qty in inventory.items():
                if qty == least_abundant_qty:
                    to_restock += item
                    count += 1
                    if count < restock_count:
                        to_restock += ", "
            print(f"Restock needed: {to_restock}")

            print("\n=== Dictionary Properties Demo ===")
            inventory_keys = ""
            count = 0
            keys_count = len(inventory.keys())
            for key in inventory.keys():
                inventory_keys += key
                count += 1
                if count < keys_count:
                    inventory_keys += ", "
            print(f"Dictionary keys: {inventory_keys}")
            inventory_values = ""
            count = 0
            values_count = len(inventory.values())
            for value in inventory.values():
                inventory_values += str(value)
                count += 1
                if count < values_count:
                    inventory_values += ", "
            print(f"Dictionary values: {inventory_values}")
            print(f"Sample lookup - 'sword' in inventory:"
                  f" {bool(inventory.get("sword"))}")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
