student_heights = input('Input a list of students heights ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)


sum_of_heights = 0
number_of_students = 0

for height in student_heights:
    sum_of_heights += height
    number_of_students += 1

print(number_of_students)
average = round(sum_of_heights / number_of_students)
print(average)

