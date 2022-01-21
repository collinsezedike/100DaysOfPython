print(4 / 2)    #produces a float

print(4 // 2)   # chops off the decimal part and produces an int

# '//' doesn't round the number; 
# it removes the decimal part, regardless of it's value 
# and returns the integer part alone

print(round(81 / 9, 2))  #rounds the digit, by default to a whole number 
# the '2' is to stipulate the required number of decimal space

a = 10
a = a + 2   # to increment a by 2

# can also be written as
 
a = 10
a += 2 

# f strings

score = 0
aggregate = 11.5
timeup = True


print('The score is ' + str(score) + ', the aggregate is ' + str(aggregate) + ' and timeup is ' + str(timeup))

# can print the above without any type casting with the use of f strings
# type casting is programming lingo for converting an object to a different data type
# example from int to str

print(f'The score is {score}, the aggregate is {aggregate} and timeup is {timeup}')

