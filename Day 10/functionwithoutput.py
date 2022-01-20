def format_name(f_name, l_name):
    return f'Hi, {f_name.title()} {l_name.title()}'
    
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')

print(format_name(f_name = first_name, l_name = last_name))
