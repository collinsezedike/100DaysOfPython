MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def check_resources_sufficiency(coffee_chosen, resources_available):
    '''Returns True or False if resources is sufficient.'''
    if coffee_chosen == 'cappuccino':
        if resources_available['water'] < 250:
            print('There is not enough water.')
            return False
        elif resources_available['milk'] < 100:
            print('There is not enough milk.')
            return False
        elif resources_available['coffee'] < 24:
            print('There is not enough coffee.')
            return False
        else:
            return True
    if coffee_chosen == 'latte':
        if resources_available['water'] < 200:
            print('There is not enough water.')
            return False
        elif resources_available['milk'] < 150:
            print('There is not enough milk.')
            return False
        elif resources_available['coffee'] < 24:
            print('There is not enough coffee.')
            return False
        else:
            return True
    if coffee_chosen == 'espresso':
        if resources_available['water'] < 50:
            print('There is not enough water.')
            return False
        elif resources_available['coffee'] < 18:
            print('There is not enough coffee.')
            return False
        else:
            return True


def add_deposits(quarters_deposited, dimes_deposited, nickels_deposited, pennies_deposited):
    '''Takes the amount of coins deposited for each denomination 
        and returns the moentary value of the total'''
    quarters_deposited *= 0.25
    dimes_deposited *= 0.10
    nickels_deposited *= 0.05
    pennies_deposited *= 0.01

    total_deposit = quarters_deposited + dimes_deposited + nickels_deposited + pennies_deposited
    return total_deposit


def check_payment(total_deposit, coffee_chosen):
    '''Returns True or False if the amount deposited is enough'''
    if coffee_chosen == 'cappuccino':
        return total_deposit >= 3.0
    elif coffee_chosen == 'latte':
        return total_deposit >= 2.5
    elif coffee_chosen == 'espresso':
        return total_deposit >= 1.5
    else:
        return False


def calculate_change(total_deposit, price_of_coffee):
    '''Calculate and returns change'''
    balance = total_deposit - price_of_coffee
    return balance


def make_coffee(resources_available, recipe):
    '''Reduces the amount of resources after coffee is made'''
    for item in recipe:
        resources_available[item] -= recipe[item]


# to terminate the program
turned_off = False
while not turned_off:
    choice_of_coffee = input('What would you like? (espresso/latte/cappuccino): ').lower()
    # to catch invalid inputs
    while choice_of_coffee not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print('Wrong input!')
        choice_of_coffee = input('What would you like? (espresso/latte/cappuccino): ').lower()

    if choice_of_coffee == 'off':
        turned_off = True
    elif choice_of_coffee == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
    else:
        enough_resources = check_resources_sufficiency(choice_of_coffee, resources)
        if enough_resources:
            print('Please insert coins.')
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))  
            nickles = int(input('How many nickels?: ')) 
            pennies = int(input('How many pennies?: '))

            total = add_deposits(quarters, dimes, nickles, pennies)
            is_transaction_successful = check_payment(total, choice_of_coffee)
            if is_transaction_successful:
                price = MENU[choice_of_coffee]['cost']
                profit += price
                change = calculate_change(total, price)
                if change != 0.0:
                    print(f'Here is your change: ${round(change, 2)}')
                make_coffee(resources, MENU[choice_of_coffee]['ingredients'])
                print(f'Here is your {choice_of_coffee}: ☕')
