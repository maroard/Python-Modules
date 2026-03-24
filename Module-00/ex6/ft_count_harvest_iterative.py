def ft_count_harvest_iterative() -> None:
    nb_days = int(input("Days until harvest: "))
    for i in range(nb_days):
        print("Day", i + 1)
    print("Harvest time!")
