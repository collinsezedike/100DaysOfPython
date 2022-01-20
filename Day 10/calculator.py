def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculator():
    # logo
    '''A recursive function'''
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input('Pick an operation from the line above: ')

    re_calculate = True
    while re_calculate:
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if cont == 'n':
            re_calculate = False
            print('Program closed')
        else:    
            num1 = answer
            operation_symbol = input('Pick an operation: ')
            calculator()
    

calculator()