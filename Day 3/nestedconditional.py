print('Welcome to the rollercoaster ride!')
height = int(input('What is your height in cm? '))

if height >= 120:
    print('You are tall enough for this ride.')
    age = int(input('What is your age? '))
    if age < 12:
        print('You get to pay $2')
    elif age <= 18:
        print('Please pay $10')
    elif age > 60:
        print('Oddies ride is $30')
    else:
        print('Pay $17')
else:
    print('Sorry! You are not tall enough for this ride.')