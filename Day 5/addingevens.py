# sum of all even numbers between 1 and 100

sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number

print(sum)