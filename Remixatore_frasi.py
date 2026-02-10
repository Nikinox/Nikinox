print('insert the letter to replace')
letter2replace = input().upper()
print('insert the letter to place in that place')
letter2place=input().upper()
print('Insert the text you wanna remix')
for i in range(2):
    tongue_twist = input().upper()
    tongue_twist=tongue_twist.replace(letter2replace, letter2place)
    print(tongue_twist)
