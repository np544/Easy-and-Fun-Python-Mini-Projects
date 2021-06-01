while True:
    n=int(input("Hey friend! Guess a number "))
    if(n%2==0):
        ch=input("That's an even number! Have another(Y/N)? ")
    else:
        ch=input("That's an odd number! Have another(Y/N)? ")
    if(ch=='N'):
        break
print("It was awesome playing with you! Have a good day!")
