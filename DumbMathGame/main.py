from random import randint

while (max := int(input("insert a maximum number\n"))) <= 1:
        print("error, insert again a > 1")
        max = int(input())

while True:

    value = randint(1, max)
    value1 = randint(1, value)

    print(value, " + ", value1, " = ")

    result = int(input())

    print("correct" if value + value1 == result else exit())
