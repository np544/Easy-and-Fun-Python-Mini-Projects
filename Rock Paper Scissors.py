from random import randint

while True:
    score=0
    choice=['rock','paper','scissors']
    computer=choice[randint(0,2)]
    player=input("Hi! Let's play Rock, Paper, Scissors!!\n To begin choose Rock, Paper or Scissor ").lower()
    print("The computer's choice is "+computer)
    if(player=='rock'):
        if(computer=='paper'):
            print('Computer is the winner!!')
        elif(computer=='rock'):
            print("Same input! Draw")
        else:
            print('You win!')
            score+=1
    elif(player=='paper'):
        if(computer=='scissor'):
            print('Computer is the winner!!')
        elif(computer=='paper'):
            print("Same input! Draw")
        else:
            print('You win!')
            score+=1
    elif(player=='scissor'):
        if(computer=='rock'):
            print('Computer is the winner!!')
        elif(computer=='scissor'):
            print("Same input! Draw")
        else:
            print('You win!')
            score+=1
    else:
        print("Invalid entry!! Check your input please.")
    ch=input('Do you want to play again?(Y/N)').lower()
    if(ch=='n'):
        print(f'It was fun playing with you!! Your score is {score}')
        break