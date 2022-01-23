# Bugged code
# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print('FizzBuzz')
#     if number % 3 == 0:
#         print('Fizz')
#     if number % 5 == 0:
#         print('Buzz')
#     else:
#         print([number])

# What it should do:
# Loop through a range of 1 and 100,
# If a number is divisible by 3, print "Fizz"
# otherwise, a number is divisble by 5, print "Buzz"
# However, if a number is divisible by both 3 and 5, print "FizzBuzz"
# otherwise, just print the number

# Problems:
# 1. it prints the numbers with '[]'
# Solution: Remove the '[]' from the print statement in the else block.

# 2. It prints "FizzBuzz" and "Fizz" or "Buzz" for numbers divisible by 3 or 5
# Solution: Change the subsequent if blocks to elifs

# 3. It doesn't print "Fizz" or "Buzz" only "FizzBuzz"
# Solution: Change the logical operator from 'or' to 'and'


# Debugged code
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)