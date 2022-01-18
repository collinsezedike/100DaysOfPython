def prime_checker(number):
    prime = []
    if number == 1:
        prime = [False]
    elif number == 2:
        prime = [True]
    # started with 2, cos every number is divisible by 1 which would have altered the code.
    for digits in range(2, number):
        if number % digits == 0:
            prime.append(False)
    if False in prime:
        print("it's not a prime number.")
    else:
        print("it's a prime number.")
        
    
n = int(input('Check this number: '))
prime_checker(number=n)
