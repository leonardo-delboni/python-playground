# TEMPERATURE CONVERSOR IN PYTHON v01
# Developed by Leonardo Travagini Delboni

# Credits:
print('\nWelcome to the TEMPERATURE CONVERSOR IN PYTHON')
print('Version 01 - v01')
print('Developed by Leonardo Travagini Delboni \n')

# Secondary Function --- Celsius to Fahrenheit:
def C_to_F(C):
    F = float((9/5)*C + 32)
    print('The temperature ' + str(C) + ' Celsius is equal to ' + str(F) + ' Fahrenheit.')
    print('In summary: '+ str(C) + ' ºC = ' + str(F) + ' ºF .\n')

# Secondary Function --- Celsius to Kelvin:
def C_to_K(C):
    K = float(C + 273.15)
    print('The temperature ' + str(C) + ' Celsius is equal to ' + str(K) + ' Kelvin.')
    print('In summary: '+ str(C) + ' ºC = ' + str(K) + ' K .\n')    

# Secondary Function --- Fahrenheit to Celsius: 
def F_to_C(F):
    C = float((5/9)*(F - 32))
    print('The temperature ' + str(F) + ' Fahrenheit is equal to ' + str(C) + ' Celsius.')
    print('In summary: '+ str(F) + ' ºF = ' + str(C) + ' ºC .\n')  

# Secondary Function --- Fahrenheit to Kelvin:
def F_to_K(F):
    K = float((5/9)*(F-32)+273.15)
    print('The temperature ' + str(F) + ' Fahrenheit is equal to ' + str(K) + ' Kelvin.')
    print('In summary: '+ str(F) + ' ºF = ' + str(K) + ' K .\n')

# Secondary Function --- Kelvin to Celsius:
def K_to_C(K):
    C = float(K - 273.15)
    print('The temperature ' + str(K) + ' Kelvin is equal to ' + str(C) + ' Celsius.')
    print('In summary: '+ str(K) + ' K = ' + str(C) + ' ºC .\n')     

# Secondary Function --- Kelvin to Fahrenheit:
def K_to_F(K):
    F = float((9/5)*(K - 273.15) + 32)
    print('The temperature ' + str(K) + ' Kelvin is equal to ' + str(F) + ' Fahrenheit.')
    print('In summary: '+ str(K) + ' K = ' + str(F) + ' ºF .\n')     

# Initial validator:
validator = 0

# Main program:
while validator == 0:

    # Inputs:
    print('Choose one of the following options: \n')
    print('    Press 0 to Quit the Program.')
    print('    Press 1 to choose C to F (CELSIUS ---> FAHRENHEIT)')
    print('    Press 2 to choose C to K (CELSIUS ---> KELVIN)')
    print('    Press 3 to choose F to C (FAHRENHEIT ---> CELSIUS)')
    print('    Press 4 to choose F to K (FAHRENHEIT ---> KELVIN)')
    print('    Press 5 to choose K to C (KELVIN ---> CELSIUS)')
    print('    Press 6 to choose K to F (KELVIN ---> FAHRENHEIT) \n')

    # Main variables:
    choice = int(input('Enter the chosen option: \n'))
    print('')

    if choice == 0:
        print('Thank you very much. See you other time! \n')
        validator = 1

    elif choice == 1:
        celsius = float(input('How many Celsius degrees do you want to convert: \n'))
        C_to_F(celsius)

    elif choice == 2:
        celsius = float(input('How many Celsius degrees do you want to convert: \n'))
        C_to_K(celsius)

    elif choice == 3:
        fahrenheit = float(input('How many Fahrenheit degrees do you want to convert: \n'))
        F_to_C(fahrenheit)

    elif choice == 4:
        fahrenheit = float(input('How many Fahrenheit degrees do you want to convert: \n'))
        F_to_K(fahrenheit)

    elif choice == 5:
        kelvin = float(input('How many Kelvin do you want to convert: \n'))
        K_to_C(kelvin)

    elif choice == 6:
        kelvin = float(input('How many Kelvin do you want to convert: \n'))
        K_to_F(kelvin)    

    else:
        print('This is not a valid function. Please try it again! \n')













