from random import randint

while (max := int(input("insert a maximum number\n"))) <= 1:
        print("error, insert again a > 1")
        max = int(input())

streak = 0

while True:

    value = randint(1, max)
    value1 = randint(1, value)

    print(value, " + ", value1, " = ")

    result = int(input())

    streak += (value + value1 == result) # if true +1, else 0, so i save an if statement and the code is shorter

    print(f"correct, streak: {streak}" if value + value1 == result else exit(f"wrong, your streak was: {streak}"))
