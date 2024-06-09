'''
currency = input('Input the currency for exchange (EUR or USD): ')
value = float(input(f'Input value of the {currency}: '))
course = 1.1
if currency.upper() == "EUR":
    new_value = value * course
else:
    new_value = round(value / course, 2)

if currency.upper() == "EUR":
    new_currecy = 'USD'
else:
    new_currency = 'EUR'

print(f'You are exchange {value} {currency.upper()} and get {new_value} {new_currency.upper()}')


value = float(input(f'Input temperature value: '))
if (value > 0 and value < 100):
    print('The water is liquid!!!')
elif value <= 0:
    print('The water is solid!!!')
else:
    print('Th water is as gas-like!!!')
'''

weight = float(input('Input the weight of person: '))
speed = float(input('Input the speed value: '))

cinetic_power = 1/2*weight*speed**2
print(cinetic_power)

