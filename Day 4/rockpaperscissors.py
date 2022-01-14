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

ascii_arts = [rock, paper, scissors]


print()
user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n>'))

# 0 beats 2, 1 beats 0, 2 beats 1
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!")
else:
    print(f'You chose: \n{ascii_arts[user_choice]}')

    computer_choice = random.randint(0,2)
    print(f'Computer chose: \n{ascii_arts[computer_choice]}')

    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == 0:
        if computer_choice == 2:
            print('You win.')
        else:
            print('You lose!')
    elif user_choice == 1:
        if computer_choice == 0:
            print('You win.')
        else:
            print('You lose!')
    elif user_choice == 2:
        if computer_choice == 1:
            print('You win.')
        else:
            print('You lose!')