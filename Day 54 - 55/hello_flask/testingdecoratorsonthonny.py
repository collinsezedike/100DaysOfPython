# def decorate(function):
#     def wrapper(*args):
#         return function(*args).title()
#     return wrapper
#
#
# @decorate
# def greet(name):
#     return name
#
#
# print(greet("angela"))


# Test 2
# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper_function(*args, **kwargs):
        print(f"You called {func.__name__}{args}")
        print(f"It returned {func(*args)}")
    return wrapper_function


# Use the decorator 👇
@logging_decorator
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
    
    
multiply(1, 2, 3)