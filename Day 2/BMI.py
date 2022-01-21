height = input('enter your height in m: ')
weight = input('enter your weight in kg: ')

BMI = float(weight) / float(height) ** 2
print(f'Your BMI is {int(BMI)}kg per square meters')
