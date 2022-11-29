import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
letters_num= int(input("How many letters would you like in your password?\n")) 
symbols_num= int(input(f"How many symbols would you like?\n"))
numbers_num = int(input(f"How many numbers would you like?\n"))


pwd=[]
print("\nYour password could be:")
for i in range(0,letters_num):
  pwd.append(random.choice(letters))
for i in range(0,symbols_num):
  pwd.append(random.choice(symbols))
for i in range(0,letters_num):
  pwd.append(random.choice(numbers))
print("".join(pwd))

print("Not satisfied with your password? Here's a more secure password for ya....")
random.shuffle(pwd)
print("".join(pwd))