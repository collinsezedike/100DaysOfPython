names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(', ')

import random


index = random.randint(0, (len(names)-1))
print(f'{names[index]} is going to pay.')