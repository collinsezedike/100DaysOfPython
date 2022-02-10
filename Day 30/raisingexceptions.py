height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters")

BMI = weight / (height ** 2)
print(f"Your BMI is {round(BMI, 2)}")
