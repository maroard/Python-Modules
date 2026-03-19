def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        f = open("../ancient_fragment.txt", "r")
        print("Connection established...\n")
        data = f.read()
        print(f"{data}\n")
        f.close()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first. ")


if __name__ == "__main__":
    main()
