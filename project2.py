import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#this the input taken
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#this is the easy version of password in particular pattern
print("this the easy version of password")
password=""

for char in range(0,nr_letters):
    password +=random.choice(letters)
for char in range(0,nr_symbols):
    password +=random.choice(symbols)
for char in range(0,nr_numbers):
    password +=random.choice(numbers)

print(password)

#this is the hard version of password
print("this is the hard version of password")
new_pass=[]

for char in range(0,nr_letters):
    new_pass.append(random.choice(letters))
for char in range(0,nr_symbols):
    new_pass.append(random.choice(symbols))
for char in range(0,nr_numbers):
    new_pass.append(random.choice(numbers))


random.shuffle(new_pass)
hard_pass=""
for char in new_pass:
    hard_pass+=char
print(hard_pass)
