tasks = 77
pouple = 13

tasks_per_pouple = tasks // pouple
print(tasks_per_pouple)

photos = 168
photos_per_list = 8
lists = photos // photos_per_list
print(lists)

cost = 45999
pay_month = 7500
month = cost // pay_month
if cost % pay_month != 0:
    month += 1
print(f'Q-ty of month is {month}')
print(f'Last month will pay: {cost % pay_month}')
