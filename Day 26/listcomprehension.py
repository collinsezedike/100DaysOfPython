# without list comprehension
numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)

# with list comprehension
new_list = [n + 1 for n in numbers]

# list comprehension syntax:
# new_list = [new_item for item in list]

# list comprehension with strings
name = "Angela"
letters_list = [letter for letter in name]
 
# list comprehension with range
new_range_list = [num *2 for num in range(1,5)]

# conditional list comprehension
# Syntax: new_list = [new_item for item in list if condition]
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in name if len(name) < 5]
long_names_all_caps = [name.upper() for name in name if len(name) > 5]