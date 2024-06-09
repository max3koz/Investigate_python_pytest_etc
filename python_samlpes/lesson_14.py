'''
for i in range(1,11):
    print(f'--- * {i} ---')
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')
'''

item = range(0, 10)
for elem in item:
    print(elem * elem)

summ = 0
for number in range(1, 101):
    summ += number
print(sum)
