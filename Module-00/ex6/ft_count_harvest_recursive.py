def print_days(current_day: int, nb_days: int) -> None:
    print("Day", current_day)
    current_day += 1
    if (current_day > nb_days):
        return
    else:
        print_days(current_day, nb_days)


def ft_count_harvest_recursive() -> None:
    print_days(1, int(input("Days until harvest: ")))
    print("Harvest time!")
