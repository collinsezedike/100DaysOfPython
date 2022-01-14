import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
'X', 'Y', 'Z']

# numbers = list(01234567890)
# why this error

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
nr_letters = int(input('How many letters would you like to have in your password?\n'))
nr_numbers = int(input('How many numbers would you like to have in your password?\n'))
nr_symbols = int(input('How many symbols would you like to have in your password?\n'))

password_selection = []
for i in range(0, nr_letters):
        password_selection += random.choice(letters)
for i in range(0, nr_numbers):
        password_selection += random.choice(numbers)
for i in range(0, nr_symbols):
        password_selection += random.choice(symbols)
# shoulda used append


random.shuffle(password_selection)
password = ('').join(password_selection)
print(f'Here is your password: {password}')