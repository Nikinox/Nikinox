while True:
    while (choice := input("choose if sorted (S) or reverse sorted (R): ").lower()) not in ["s", "r"]:
        print("error, insert again the choice")

    words = input("insert dividing with spaces:\n").split()

    print(" ".join(sorted(words)) if choice == "s" else " ".join(sorted(words, reverse=True)))
