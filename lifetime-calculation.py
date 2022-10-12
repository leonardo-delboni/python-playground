print('Lifetime until now!')
print('Developed by Leonardo Travagini Delboni \n')

#Libraries used:
from datetime import datetime
from datetime import date
from dateutil import relativedelta

def new_user():

    # User first and last names:
    print('Welcome new user! Please insert the following information below:\n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')

    # User birthday, month and year:
    print('For the following three questions, please provide them in number format: \n')
    birth_day = int(input('What is the day when you were born? \n'))
    birth_month = int(input('What is the month when you were born? \n'))
    birth_year = int(input('What is the year when you were born? \n'))
    birth_date = date(birth_year, birth_month, birth_day)
    print('\n')

    # Current moment information:
    current_day = datetime.now().day
    current_month = datetime.now().month
    current_year = datetime.now().year
    current_date = date(current_year, current_month, current_day)

    # Calculating the total amount of days:
    quantity_days = (current_date - birth_date).days

    # Calculating the amount of years, months and days:
    quantity_years = int(quantity_days/365)
    rest_1 = float(quantity_days/365) - float(quantity_years)
    rest_years_in_days = int(rest_1*365)

    quantity_months = int(rest_years_in_days/30)
    rest_2 = float(rest_years_in_days/30) - float(quantity_months)
    rest_months_in_days = int(rest_2*30)
    
    rest_days = rest_months_in_days

    # Converting to strings:
    quantity_years = str(quantity_years)
    quantity_months = str(quantity_months)
    quantity_days = str(quantity_days)
    rest_days = str(rest_days)

    # Printing the results:
    print('Nice to meet you ' + first_name + ' ' + last_name + '!')
    print('You have already lived ' + quantity_years + ' years, ' + quantity_months + ' months, and ' + rest_days + ' days.')
    print('Congratulations! You have lived in total ' + quantity_days + " days until now!\n")

new_user()