immutable_var = 1, 2, 3, True, "String"
print('immutable_var', immutable_var)

# immutable_var [0] = 200   кортеж нельзя редактировать или как-либо изменять.
# Зачастую он используется в качестве хранилища, например, для какого-то списка,
# который мы ни коим образом не хотим трогать, то есть нам нужно чтобы он оставался неизменным.
# print(immutable_var)

mutabel_list = [[1, 2, 3, True, "string"], 9, 8, 7, 'kirill']
print(mutabel_list)
mutabel_list[0][0] = '9'
mutabel_list[0][1] = '8'
mutabel_list[0][2] = '7'
mutabel_list[0][3] = '2024'
mutabel_list[0][4] = 'Кирилл'
mutabel_list[-4] = '1'
mutabel_list[-3] = '2'
mutabel_list[-2] = '3'
mutabel_list[-1] = True
print(mutabel_list)
