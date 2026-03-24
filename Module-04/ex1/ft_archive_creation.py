def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    print("Initializing new storage unit: new_discovery.txt")
    with open("new_discovery.txt", "w") as f:
        print("Storage unit created successfully...\n")

        data = (
            "[ENTRY 001] New quantum algorithm discovered\n"
            "[ENTRY 002] Efficiency increased by 347%\n"
            "[ENTRY 003] Archived by Data Archivist trainee"
        )

        print("Inscribing preservation data...")
        print(data)
        f.write(data)

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
