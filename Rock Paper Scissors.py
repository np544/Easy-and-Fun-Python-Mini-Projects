import random 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    score=0
    choice=int(input("Hi! Let's play Rock, Paper, Scissors!!\n To begin choose 0 for Rock, 1 for Paper or 2 for Scissor "))
      

    options=[rock,paper,scissors]
    cchoice=random.choice(options)

    if(choice==0):
      print("Your choice:",rock)
      print("Computers choice:\n",cchoice)
      if(cchoice==scissors):
       print("You win")
       score+=1
      elif(cchoice==rock):
       print("Draw!")
      else:
       print("You lose")
    elif(choice==1):
      print("Your choice:",paper)
      print("Computers choice:\n",cchoice)
      if(cchoice==rock):
       print("You win")
       score+=1
      elif(cchoice==paper):
       print("Draw!")
      else:
       print("You lose")
    elif(choice==2):
      print("Your choice:",scissors)
      print("Computers choice:\n",cchoice)
      if(cchoice==paper):
       print("You win")
       score+=1
      elif(cchoice==scissors):
       print("Draw!")
      else:
       print("You lose")
    else:
        print("Invalid input, You lose")

    ch=input('Do you want to play again?(Y/N)').lower()
    if(ch=='n'):
        print(f'It was fun playing with you!! Your score is {score}')
        break