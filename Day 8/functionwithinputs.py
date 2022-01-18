# function review
def greet():
    print('Hello!')
    print('This is a greet function.')
    print('Bye!')

greet()

# function that allow input
def greet_with_name(name):
    print(f'Hello! {name}')
    print(f'How do you do {name}')
    print("Isn't the weather lively today?")

greet_with_name('Angela')

# function with multiple inputs
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

# positional arguments call
greet_with('Angela', 'London')
# call with keyword argument
greet_with(location='Nowhere', name='Jack Bauer')
