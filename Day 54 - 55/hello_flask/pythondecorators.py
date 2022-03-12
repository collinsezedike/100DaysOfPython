# Functions can have functionality/inputs/outputs
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions can be passed as arguments
def calculate(calc_func, n1, n2):
    return calc_func(n1, n2)


result = calculate(add, 2, 3)
print(result)


# Functions can be nested inside another function
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


# the outer function will return a nested function object
inner_function = outer_function()
print(type(inner_function))
