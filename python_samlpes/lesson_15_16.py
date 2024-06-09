from copy import deepcopy

#currency = {'USD': 38, 'Euro': 39, 'PLN': 4}
#print(type(currency))
#print(currency)

#d = {'name': 'John Doe',  'age': 30, 'city': 'New York', 'email': 'johndoe@example.com'}
#del_key = input('Input the key which you want to delet: ')
#d.pop(del_key)
#print(d)

#d = {'name': 'Alice Smith',
#     'age': 25,
#     'city': 'Los Angeles',
#     'email': 'alice.smith@example.com',
#     'favorite_subjects': ['Mathematics', 'History', 'Literature']
#     }
#for elem in d.get('favorite_subjects'):
#     print(elem)

favorites = {
    'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
    'music': ['Queen', 'The Beatles', 'Coldplay'],
    'sports': ['football', 'basketball', 'tennis']
}

new_favorites = deepcopy(favorites)
new_favorites.pop('sports')
new_favorites['serials'] = ['frends', 'monki']
print(favorites)
print(new_favorites)
