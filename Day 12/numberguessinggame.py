import random
from numberguessinggame_art import logo

def choose_num(guess_range):
    '''Takes a range and returns a random number within that range'''
    random_num = random.randint(1, guess_range)
    return random_num

def check(guess, secret_num):
    '''Takes the guess and evaluates if it is correct'''
    if guess == secret_num:
        is_correct = True
        return [f'You got it. I thought of {secret_num}. You win!', is_correct]
    else:
        is_correct = False
        if guess > secret_num:
            return ['Too high', is_correct]
        elif guess < secret_num:
            return ['Too low', is_correct]
    
def num_of_trials(level):
    '''Takes the level chosen and returns the appropriate number of trials'''
    if level == 'easy':
        return 10
    else:
        return 5
    

guess_range = 100
trials = 0

print(logo)
print('Welcome to the Number Guessing Game.\n')
print("I'm Jonathan, the quiz master.")
print(f"I'm gonna think of a number between 1 and {guess_range}")
print("Can you guess it?\n")
print('What level would you like to play at?')
print("Type 'easy' to play at an easy level. Type 'hard' to play at a hard level.")

wrong_input = True
while wrong_input:
    level_chosen = input('>').lower()
    if level_chosen == 'easy' or level_chosen == 'hard':
        wrong_input = False
        trials = num_of_trials(level_chosen)
    else:
        wrong_input = True
        print('Wrong level!')

print(f'\n{level_chosen} level it shall be.')
print("I'm gonna think of a number now. Goodluck!\n")
secret_num = choose_num(guess_range)
print("I have thought of a number")

guess_is_correct = False
while not guess_is_correct and trials != 0:
    if trials == 1:
        print(f"You have {trials} attempt to guess the number.")
    else:
        print(f"You have {trials} attempts to guess the number.")
    guess = int(input('\nMake a guess: '))
    result = check(guess, secret_num)
    if result[1]:
        print(result[0])
        guess_is_correct = True
    else:
        trials -= 1
        print(result[0])
if trials == 0:
    print("\nYou ran of trials. You lose")
