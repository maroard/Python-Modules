def handle_archive_access(filename: str, alert_message: str,
                          status_message: str) -> None:
    try:
        print(f"{alert_message} '{filename}'...")
        with open(filename, "r") as f:
            data = f.read()
            print(f"SUCCESS: Archive recovered - {data}")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception:
        print("RESPONSE: An error occurred")
    print(status_message)
    print()


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    handle_archive_access(
        "lost_archive.txt",
        "CRISIS ALERT: Attempting access to",
        "STATUS: Crisis handled, system stable"
    )

    handle_archive_access(
        "classified_vault.txt",
        "CRISIS ALERT: Attempting access to",
        "STATUS: Crisis handled, security maintained"
    )

    handle_archive_access(
        "standard_archive.txt",
        "ROUTINE ACCESS: Attempting access to",
        "STATUS: Normal operations resumed"
    )

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
