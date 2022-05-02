def my_func(num_1, num_2):
    res_dev = num_1 / num_2
    return res_dev
try:
    print(my_func(float(input("Укажите число номер 1: ")), float(input("Укажите число номер 2: "))))
except ZeroDivisionError as er:
    print(er)