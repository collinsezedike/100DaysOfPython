# Bugged code
year = input('Which year do you want to check? ')
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('Leap year.')
#         else:
#             print('Not a leap year.')
#     else:
#         print('Leap year.')
# else:
#     print('Not a leap year.')

# Problem:
# TypeError: not all arguments converted during string formatting
print(type(year))
# Trying to perform arithmetic operation on a string

# Debugged code
year = int(input('Which year do you want to check? '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not a leap year.')
    else:
        print('Leap year.')
else:
    print('Not a leap year.')