# Get the right emoji

# 1. Describe problem
def my_function():
    for i in range(1,20):
        if i == 20:
            print('You got it.') 
my_function()

# Problem Description: 
# I created a function that when called, 
# loops through a range of 1 and 20.
# When at 20, it should print 'you got it'
# However, nothing is printed on the console when I call the function.
# I am assuming that i would reach 20 however, it doesn't.
# This is because the range function excludes the upper bound.

# Solution:
# Increase the upper bound so that i would actually reach 20 
def my_function():
    for i in range(1,21):
        if i == 20:
            print('You got it.') 
my_function()

# 2. Reproduce the bug
from random import randint
dice_imgs = ['1', '2', '3', '4', '5', '6']      # get the right emoji
dice_num = randint(1,6)
print(dice_imgs[dice_num])

#reproducing the bug:
from random import randint
dice_imgs = ['1', '2', '3', '4', '5', '6']      # get the right emoji
# dice_num = 6
# print(dice_imgs[dice_num])

# The error shows up saying an IndexError
#  The index given to dice_imgs is out of range
# because the rnadint function occasionally returns 6
# which is out of the list index range

# Solution:
# Change the bounds of the randint function to 0 and 5
from random import randint
dice_imgs = ['1', '2', '3', '4', '5', '6']      # get the right emoji
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# 3. Play computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You're a millenial.")
elif year > 1994:
    print('You are Gen Z.')

# inputing 1994 would not print anything
# because there is no condition that catches it.
# The if checks for if the year is LESS THAN 1994,
# the elif checks for years that are GREATER THAN 1994.

# Solution:
# Change the comparison operator in the elif block from > to >=
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
    print("You're a millenial.")
elif year >= 1994:
    print('You are Gen Z.')

# 4. Fix the Errors
# age = input('How old are you? ')
# if age > 18:
# print('You can drive at age {age}')

# Firstly, the editor is highlighting that 
# the print statement following the if statement was not indented.
# This is one advantage of using editors

# Solution:
# # Indent the print statement
# age = input('How old are you? ')
# if age > 18:
#     print('You can drive at age {age}')

# Secondly, the consolle shows this error: 
# TypeError: '>' not supported between instances of 'str' and 'int'
# Copy the error message and search on google 
# age is a string and cannot be arithmetically compared with 18

# Solution: 
# Cast the age into an integer
age = int(input('How old are you? '))
if age > 18:
    print('You can drive at age {age}')

# Finaly, nothing is wrong with the code syntactically
# However, it doesn't output as expcted.

# Solution
# Change the print statement to an f-string
age = int(input('How old are you? '))
if age > 18:
    print(f'You can drive at age {age}')

# 5. Print is your friend
pages = 0 
word_per_page = 0
pages = int(input('Number of pages: '))
word_per_page == int(input('Number of words per page: '))
total_words =  pages * word_per_page
print(total_words)

# Use print statements to print variables and see if they are what you intended
pages = 0
print(f' pages = {pages}')
word_per_page = 0
print(f'Words per page = {word_per_page}')
pages = int(input('Number of pages: '))
print(f' pages = {pages}')
word_per_page == int(input('Number of words per page: '))
print(f'Words per page = {word_per_page}')
total_words =  pages * word_per_page
print(f'total words = {total_words}')

# everything worked fine till: 
# word_per_page == int(input('Number of words per page: '))

# Solution:
# Change the '==' to '='
pages = 0 
word_per_page = 0
pages = int(input('Number of pages: '))
word_per_page = int(input('Number of words per page: '))
total_words =  pages * word_per_page
print(total_words)

# 6. Use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

# Paste the code on a visual debugger like Thonny or Pythontutor.com
# And watch how your code runs, step by step.
# b_list.append(new_item) is not indented,
# so it only appends the the last item from the loop

# Solution:
# indent b_list.append(new_item)
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])

# 7. Take a break
# 8. Ask a friend
# 9. Run often
# 10. Ask Stack Overflo
