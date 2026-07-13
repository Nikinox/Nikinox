while True:
    while (choice := input("choose if sorted (S) or reverse sorted (R): ").lower()) not in ["s", "r"]:
        print("error, insert again the choice")

    print(" ".join(sorted(input("insert with spaces:\n").split())) if choice == "s" else " ".join(sorted(input("insert with spaces:\n").split(), reverse=True)))
