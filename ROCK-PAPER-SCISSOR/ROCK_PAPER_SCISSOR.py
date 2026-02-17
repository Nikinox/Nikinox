from random import randint

print('Welcome to ROCKPAPERSCISSOR!')

print('-------------------------------------')
print('enter 1 to play; 0 to exit')
c = int(input())

while c not in (0, 1):
    print("insert a valid answer")
    c = int(input())

while c == 1:   # ciclo principale del gioco
    # Game
    print('SELECT YOUR CHOICE: rock, paper, scissor')
    x = input().lower()

    while x not in ("rock", "paper", "scissor"):
        print("insert a valid choice")
        x = input().lower()

    y = randint(0, 2)
    cpu_move = ["rock", "paper", "scissor"][y]
    print("computer move is", cpu_move)

    # Results
    if x == cpu_move:
        print("Result = TIE")
    elif (x == "rock" and cpu_move == "scissor") or \
         (x == "paper" and cpu_move == "rock") or \
         (x == "scissor" and cpu_move == "paper"):
        print("Result = YOU WON")
    else:
        print("Result = CPU WON")

    print('-------------------------------------')
    print('enter 1 to play; 0 to exit')
    c = int(input())

    while c not in (0, 1):
        print("insert a valid answer")
        c = int(input())

    if c == 0:
        print("thanks for playing")
        break
