import random
from hangman_wordlist import word_list
from hangman_art import logo, stages
chosen_word = random.choice(word_list).upper()
display = []
for _ in chosen_word:
    display.append('_')
end_of_game = False
lives = 6

print(logo)

guessed_letters = []
while not end_of_game:

    guess = input('\nGuess a letter: ').upper()
    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess
    print('\n'+' '.join(display)+'\n')

    if guess in guessed_letters and guess != '':
        print(f'You already guessed {guess}')
    else:
        guessed_letters.append(guess)
  

    if guess not in chosen_word:
        print(f'{(guess)} is not in the word. You lose a life.')
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('You lost all lives. You lose.')

    
    if '_' not in display:
        end_of_game = True
        print(f'You guessed the word. {chosen_word}. You win!')
