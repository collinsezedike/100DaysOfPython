# Import the random module
import random
# Import the arts
from higherorlower_arts import logo, vs
# Import game data
from higherorlower_data import data


# Display the comparisons
## Create a function that randomly chooses the accounts for comparison
def pick_options():
    '''Returns a random account'''
    return random.choice(data)

# Checks if answer is correct
## A function that takes the user choice as input and returns if answer is correct or wrong
## Hint: Look at the followers key
def check_answer(choice, accountA, accountB):
    '''Takes the user's choice and the accounts being compared and returns True or False if user's choice is correct'''
    if choice == 'A' and (accountA['follower_count'] > accountB['follower_count']):
            return True
    elif choice == 'B' and (accountB['follower_count'] > accountA['follower_count']):
            return True
    else:
        return False

# Keep recrod of the score
score = 0

# this should be outside of the loop
print(logo)
# pick an account for A
celebrityA = pick_options()



# Loop until answer is wrong
is_correct = True
while is_correct:
    # Format how the comparison would be displayed
    print(f"Compare A: {celebrityA['name']}, a {celebrityA['description']}, from {celebrityA['country']}.") 
    print(vs)
    # pick an account for A
    celebrityB = pick_options()
    # pick again if the program gives the same account for comparison
    while celebrityB == celebrityA:
        celebrityB = pick_options()
    # Format how the comparison would be displayed
    print(f"Against B: {celebrityB['name']}, a {celebrityB['description']}, from {celebrityB['country']}.")
    
    
    # Receive input: Who has more followers? Type 'A' or 'B':
    user_choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    # checks if answer is correct
    is_correct = check_answer(user_choice, celebrityA, celebrityB)

    # If correct add 1 to score.
    ## Print: You're right! and the current score
    if is_correct:
        score += 1
        print(f"You're right!. Current score: {score}\n")
        
        # Game restarts here
        # print(logo)
        # make the previous B the new A
        celebrityA = celebrityB
        print(logo)

    # Else, game over.
    ## Print: Sorry, that's wrong and the Final score
    else:
        print(f"Sorry, that's wrong. Final score: {score}")