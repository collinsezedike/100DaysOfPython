import random

# random integer 
random_interger = random.randint(1,10)
print(random_interger)

# random float between 0 and 1
random_float = random.random()
print(random_float)

# random float between 1 and 5
# I googled this
random_float = random.uniform(1,5)
print(random_float)
# Angela's style
random_float = random.random()
print(random_float*5)

# a random love score generator
love_score = random.randint(1,100)
print(f'Your love score is {love_score}%')
