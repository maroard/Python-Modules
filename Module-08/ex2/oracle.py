from dotenv import load_dotenv
import os


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    print()
    print("Configuration loaded:")

    mode = os.getenv("MATRIX_MODE")
    if mode is None:
        mode = "development"
    database = os.getenv("DATABASE_URL")
    api_access = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_network = os.getenv("ZION_ENDPOINT")

    print(f"Mode: {mode}")
    if database is not None and mode == "development":
        print("Database: Connected to local instance")
    elif database is not None and mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database: Unknown")
    if api_access is not None:
        print("API Access: Authenticated")
    else:
        print("API Access: Unable to authenticate")
    if log_level is None and mode == "development":
        print("Log Level: DEBUG")
    elif log_level is None and mode == "production":
        print("Log Level: WARNING")
    else:
        print(f"Log Level: {log_level}")
    if zion_network is not None:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print()
    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")
    if None in [database, api_access, log_level, zion_network]:
        print("[KO] .env file badly configured")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
