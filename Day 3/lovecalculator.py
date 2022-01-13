print('Welcome to the love calculator')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')

name1 = name1.lower()
name2 = name2.lower()
both_names = name1 + name2

tens_digit = both_names.count('t') + both_names.count('r') + both_names.count('u') + both_names.count('e')
unit_digit = both_names.count('l') + both_names.count('o') + both_names.count('v') + both_names.count('e')

score = f'{tens_digit}{unit_digit}'
score = int(score)

if score < 10 or score > 90:
    print(f'Your score is {score}%, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is {score}%, you are alright together.')
else:
    print(f'Your score is {score}%')

