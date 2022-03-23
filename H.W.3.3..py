def my_func(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 - (min(num_1, num_2, num_3))
print(my_func(int(input('Введите число номер 1: ')), int(input('Введите число номер : ')), int(input('Введите число номер 3: '))))
