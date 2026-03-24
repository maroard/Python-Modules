import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release", "use"]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()

    for i in range(1000):
        name, action = next(event_stream)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for i in range(10):
        events.append(next(event_stream))
    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
