# E-mail with termination in '.com' Checker
# Developed by Leonardo Travagini Delboni

# Credits:
print('')
print('E-mail with final .com Checker \nDeveloped by Leonardo Travagini Delboni \n')

# Input:
email = input('Please, insert below the e-mail to be checked. \nTry to insert it the format xxx@xxx.com: \n')
print('')

# Auxiliars:
size = len(email)
validation = 0
email_list =[]

# Based on g-mail creation rules (https://support.google.com/mail/answer/9211434?hl=pt-BR):]

if email.count('@') != 1:
    validation += 1
    print('Not a valid e-mal! Try it again. \n')

else:
    
    # Only a single '@':
    email_list = email.split('@')
    termination = email_list[1]

    # Maximum of a single '.' in the first part:
    if email_list[0].count('.') > 1:
        validation += 1
        print('Not a valid e-mal! Try it again. \n')
    
    # Checking the presence of forbidden characters:
    forbidden_single_list = [' ', '=', '+', '<', '>', '{', '}', '[', ']', '^', '~', '?', '/', '!']
    for i in email:
        for j in forbidden_single_list:
            if i == j or j == i:
                validation += 1
    if validation > 0:
        print('Not a valid e-mal! Try it again. \n')

    # Checking the second part - after the '@':
    second_part = email_list[1].split('.')
    size_second_part = len(second_part)
    if len(second_part) <= 1:
        validation += 1
        print('Not a valid e-mal! Try it again. \n')

    # Not finished in '.com':    
    if second_part[size_second_part-1] != 'com':
        print('This e-mail is not finished with .com. Please, try to use one with .com.')

    # Final validation:
    if validation == 0:
        print('The e-mail {0}, apparently is a possible e-mail, with termination {1}'.format(email, termination))

# Final regards:
print('Thank you very much! \n')
