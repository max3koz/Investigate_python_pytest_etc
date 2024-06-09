my_list = [5, 3, 4, 2, 5]
new_list = []
for elem in my_list:
    if elem > 3:
        new_list.append(elem)
new_list.sort()
print(new_list)

list_1 = ['lemon', 'banana', 'lime']
list_2 = ['tea', 'coffee', 'suger']
list_1.extend(list_2)
new_list = list_1
print(new_list)
for elem in new_list:
    print(f'{elem}: {len(elem)}')
new_list.sort(key=len)
print(new_list)
new_list.sort(key=len, reverse=True)
print(new_list)
