def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    player_datas = {
        "alice": {"score": 2300, "active": True,
                  "achievements": ("first kill", "level 10", "boss slayer"),
                  "region": "north"},
        "bob": {"score": 1800, "active": True,
                "achievements": ("first kill", "level 10"),
                "region": "south"},
        "charlie": {"score": 2150, "active": True,
                    "achievements": ("first kill", "level 10", "boss slayer",
                                     "collector", "perfectionist"),
                    "region": "east"},
        "diana": {"score": 2050, "active": False,
                  "achievements": ("first kill", "gun master"),
                  "region": "central"},
    }

    print("=== List Comprehension Examples ===")
    high_scorers = [player for player, data in player_datas.items()
                    if data["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubled = [data["score"] * 2 for player, data
                      in player_datas.items()]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [player for player, data
                      in player_datas.items() if data["active"] is True]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    scores = {player: data["score"] for player, data
              in player_datas.items()}
    print(f"Player scores: {scores}")
    score_categories = {
        "high": len([player for player, data in player_datas.items()
                     if data["score"] > 2000]),
        "medium": len([player for player, data in player_datas.items()
                       if data["score"] < 2000 and data["score"] > 1000]),
        "low": len([player for player, data in player_datas.items()
                    if data["score"] < 1000])
    }
    print(f"Score categories: {score_categories}")
    achievement_counts = {player: len(data["achievements"]) for player, data
                          in player_datas.items()}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {player for player, data in player_datas.items()}
    print(f"Unique players: {unique_players}")
    unique_achievements = {achievement for player, data in player_datas.items()
                           for achievement in data["achievements"]}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {data["region"] for player, data in player_datas.items()
                      if data["active"] is True}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    total_score = sum([data["score"] for player, data in player_datas.items()])
    print(f"Average score: {total_score / len(unique_players)}")
    top_performer = max(player_datas, key=lambda player:
                        player_datas[player]["score"])
    print(f"Top performer: {top_performer}"
          f" ({player_datas[top_performer]["score"]} points"
          f", {len(player_datas[top_performer]["achievements"])}"
          " achievements)")


if __name__ == "__main__":
    main()
