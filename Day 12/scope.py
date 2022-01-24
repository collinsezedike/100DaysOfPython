enemies = 1

def increase_enemies():
    enemies = 2
    print(f'enemiese inside the function: {enemies}')

increase_enemies()
print(f'enemiese outside the function: {enemies}')

# Local scope
def drink_potion():
    potion_strenght = 2     # Local variable
    print(potion_strenght)
drink_potion()
# print(potion_strength)  # produce a nameerror

# Global scope
player_health = 10      # Global variable

def drink_potion():
    potion_strenght = 2
    print(player_health)

drink_potion()

# Block scope
game_level = 3
enemies = ['Skeleton', 'Zombie', 'Alien']
if game_level < 5:
    new_enemy = enemies[0]
    # new_enemy is not local to the if block
    # because there is no such thing as block scope in Python
print(new_enemy)
# Likewise while and for loops blocks

# Modifying Global scope
enemies = 1
friends = 0
def increase_enemies():
    enemies = 2     # this doesn't modify the enemies variable rather, creates a new one
    
    # to modify a global variable:
    global friends 
    friends += 1     # writing this line without the above line will produce an error
    # because functions only work with localized variables 
    print(f'enemiese inside the function: {enemies}')

increase_enemies()
print(f'enemiese outside the function: {enemies}')
