from random import randint


print('Insert your name so BauGPT can chat with you')
name = input()

else:   
    print("Hi " +name+"!Nice to meet you")

print("Chat in English")
while True:
    user_message=str(input())
    number_baus = randint(1,99)
    print('')
    for i in range(number_baus):
        if number_baus >=50:
            print('BAU!')
        else:
            print('bau')
    if 'cat' in user_message.lower():
        if randint(0,1)==0:
            print('miao')
        else:
            print('MIAO!')
    if 'food' in user_message.lower():
        print('BAUU BAU BAUUUU :)')
    if 'sleep' in user_message.lower():
        print('BAu... zzz')
    if 'bad dog' in user_message.lower():
        for i in range(randint(1,10)):
            print('GRRR... BAU BAU!! >:( ')
