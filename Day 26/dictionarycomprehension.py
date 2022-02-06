# dictionary comprehension  

# creating new dictionary from a list
# syntax:
# new_dict = {new_key:new_value for item in list}
import random
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)


# creating new dictionary from a dictionary
# syntax:
# new_dict = {new_key:new_value for (key, value) in dictionary.items()}

# conditional dictionary comprehension
# syntaxes:
# new_dict = {new_key:new_value for item in list if condition}
# new_dict = {new_key:new_value for (key, value) in dictionary.items() if condition}
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)


