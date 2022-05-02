my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите целое положительное число: '))
my_list.append(new_el)
my_list.sort(reverse=True)
print(my_list)