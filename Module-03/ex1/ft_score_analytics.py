import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score 1> <score 2> ...")
    else:
        args = sys.argv[1:]
        try:
            scores = []
            for arg in args:
                scores.append(int(arg))
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError as error:
            print(f"Error: {error}")
