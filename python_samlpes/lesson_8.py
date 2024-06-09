string = input('Enter the string:')
# Task_1
print(string.upper())

# Task_2
if string.find('a') != -1:
    new_string = string.replace('a', '*')
    print(f'The updated string is: {new_string}')
else:
    print('The "a" is not entry in the string')

# Task_3
letters = len(string)
print(f'The string is consist of {letters} letter')
