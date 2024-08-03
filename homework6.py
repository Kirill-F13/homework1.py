my_dict = {'Misha': 1974, 'Tanya': 1975, 'book': 2000, 'Kirill': 1993, 'Varvara': 2011}
print(my_dict)
print(my_dict['Varvara'])
my_dict['book'] = 2024
print(my_dict)
my_dict['Max'] = 1992
print(my_dict)
my_dict.update({'Ulya': 1992,
                'Alex': 1991,
                'Vitya': 1990})
print(my_dict)
a = my_dict.pop('Alex')
print(my_dict)
print(a)
print(my_dict.get('vasya'))
print(my_dict.get('vasya', 'Такого ключя нет'))
del my_dict['book']
print(my_dict)

print()
print()
print()

my_set = {1, 'Яблоко', 42.13, 1, 1, 1, 2, 3, 3, 2, 42, 13, 42.13, True}
print(my_set)
my_set.add((7, 'max'))
print(my_set)
my_set.discard(42)
print(my_set)
my_set.remove(13)
print(my_set)
