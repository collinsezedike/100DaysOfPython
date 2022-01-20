def is_leap(year):
    '''Checks if a year is a leap year'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
           return True
    else:
        return False

def days_in_month(year, month):
    '''Returns the number of days in a month'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        if month ==  2:
            return 29
    else:
        return month_days[month -  1]

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = days_in_month(year, month)
print(days)