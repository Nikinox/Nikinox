#idea presa da Github
#link:https://github.com/garimasingh128/awesome-python-projects/blob/master/ROCK_PAPER_SCISSOR/ROCKPAPERSCISSOR.py
from random import randint

print('Welcome to ROCKPAPERSCISSOR!')
player = False
print('Enter the numbers of time you want to play aumented by 1')
number_times=int(input())
for i in range(number_times):
    while player == False:
        print('-------------------------------------')
        print('enter 1 to play;0 to exit')
        c = int(input())
        if c not in(0, 1):
            print('ERROR!REBOOT THE GAME AND INSERT A VALID NUMBER')
        if(c==0):
            print('thanks for playing')
            break
        elif(c==1):
            print('SELECT YOUR CHOICE rock paper scissor')
            x=str(input().lower())
            y=randint(0, 2)
        if y==0:
            print("computer move is rock")
        elif y==1:
            print("computer move is paper")    
        elif y==2:
            print("computer move is scissor")    
        if (x=="rock" and y==0):
            print("Result= TIE")    
        elif (x=="rock" and y==1):
            print("Result= CPU WON ")   
        elif (x=="rock" and y==2): 
            print("Result= YOU WON")    
        elif (x=="paper" and y==0):
            print("Result= YOU WON")   
        elif (x=="paper" and y==1):
            print("Result= TIE ")    
        elif (x=="paper" and y==2): 
            print("Result= CPU WON")    
        elif (x=="scissor" and y==0):
            print("Result= CPU WON")    
        elif (x=="scissor" and y==1):
            print("Result= YOU WON ")   
        elif (x=="scissor" and y==2): 
            print("Result= TIE")

    else:
          print("That's not a valid play. Check your spelling!")
          player = False
          y =randint(0,2)

else:
    print('ERROR')
         
