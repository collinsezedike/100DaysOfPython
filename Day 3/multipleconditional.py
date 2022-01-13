print('Welcome to the rollercoaster ride!')
height = int(input('What is your height in cm? '))
bill = 0 

if height >= 120:
    print('You are tall enough for this ride.')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 2
        print('Kiddies ticket is $2')
    elif age <= 18:
        bill = 10
        print('Teenagers are to pay $10')
    elif age > 60:
        bill = 30
        print('Oddies ride is $30')
    else:
        bill = 17
        print('Every other age group is to pay $17')

    want_photo = input('Do you want a photo taken? (y/n) ')
    if want_photo == 'y':
        bill += 3

    print(f'Please pay ${bill} for the ride.')
else:
    print('Sorry! You are not tall enough for this ride.')