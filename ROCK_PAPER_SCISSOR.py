from random import randint

print('Welcome to ROCKPAPERSCISSOR!')

while True:
    print('-------------------------------------')
    print('enter 1 to play; 0 to exit')
    c = int(input())

    if c == 0:
        print('thanks for playing')
        break

    if c != 1:
        print('ERROR! Insert 1 or 0')
        continue

    # Gioco
    print('SELECT YOUR CHOICE: rock, paper, scissor')
    x = input().lower()

    if x not in ("rock", "paper", "scissor"):
        print("That's not a valid play. Check your spelling!")
        continue

    y = randint(0, 2)
    cpu_move = ["rock", "paper", "scissor"][y]
    print("computer move is", cpu_move)

    # Risultati
    if x == cpu_move:
        print("Result = TIE")
    elif (x == "rock" and cpu_move == "scissor") or \
         (x == "paper" and cpu_move == "rock") or \
         (x == "scissor" and cpu_move == "paper"):
        print("Result = YOU WON")
    else:
        print("Result = CPU WON")
