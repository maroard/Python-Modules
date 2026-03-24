def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")

    try:
        with open("classified_data.txt", "r") as f:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("ERROR: Vault data not found")
    except PermissionError:
        print("ERROR: Access denied to vault")
    except Exception:
        print("ERROR: Unexpected vault failure")

    try:
        with open("security_protocols.txt", "w") as f:
            print("\nSECURE PRESERVATION:")
            data = "[CLASSIFIED] New security protocols archived"
            print(data)
            f.write(data)
    except PermissionError:
        print("ERROR: Cannot write security protocols")
    except Exception:
        print("ERROR: Unexpected error during preservation")

    print("\nVault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
