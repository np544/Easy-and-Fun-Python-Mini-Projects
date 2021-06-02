from random import randint

while True:
    count=0
    num=randint(1,51)
    while True:
        guess=int(input('Guess a number between 1 and 50. If you are want to give up, enter 0\n '))
        if(guess==num):
            print(f"You got it right! Congratulations!! You guessed it in {count} guesses.")
            break
        elif(guess==0):
            print(f'Okey! The number to be guessed is {num}')
            break
        elif(guess<num):
            print('Guess higher')
            count+=1
        elif(guess>50 or guess<1):
            print('You need to guess between 1 and 50 dear friend!')
        else:
            print('Guess lower')
            count+=1
    ch=input('It was super fun playing with you. Want to play again?(Y/N) ').lower()
    if(ch=='n'):
        break
     
