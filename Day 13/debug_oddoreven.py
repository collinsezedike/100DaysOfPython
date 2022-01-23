# Bugged code:
# number = int(input('Which number do you want to check? '))

# if number % 2 = 0:
#     print('This is an even number.')
# else:
#     print('This is an odd number.')

# Problem: 
# The single equal to sign is to assign not to evaluate

# Debugged code:
number = int(input('Which number do you want to check? '))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')