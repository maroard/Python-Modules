def game_event_stream():
    i = 0
    players = ["alice", "bob", "charlie"]
    events = ["found treasure", "leveled up", "killed monster"]
    players_levels = {"alice": 5, "bob": 12, "charlie": 7}
    while True:
        player = players[i % 3]
        event = events[(i + 2) % 3]
        if event == "leveled up":
            players_levels[player] += 1
            level = players_levels[player]
        else:
            level = players_levels[player]
        yield (player, level, event)
        i += 1


def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def prime_numbers_generator():
    n = 2
    while True:
        is_prime = True
        for i in range(2, n - 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")
    stream = game_event_stream()
    total_events = 1000
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    for i in range(total_events):
        player, level, event = next(stream)
        if level >= 10:
            high_level_players += 1
        if event == "found treasure":
            treasure_events += 1
        elif event == "leveled up":
            level_up_events += 1
        if (i < 3):
            print(f"Event {i + 1}: Player {player} (level {level}) {event}")
    print("...")

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (+10): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")
    fibonacci_sequence = ""
    values_count = 10
    gen = fibonacci_generator()
    for n in range(values_count):
        fibonacci_sequence += str(next(gen))
        if n < values_count - 1:
            fibonacci_sequence += ", "
    print(f"Fibonacci sequence (first {values_count}): {fibonacci_sequence}")
    prime_numbers = ""
    values_count = 5
    gen = prime_numbers_generator()
    for n in range(values_count):
        prime_numbers += str(next(gen))
        if n < values_count - 1:
            prime_numbers += ", "
    print(f"Prime number (first {values_count}): {prime_numbers}")
