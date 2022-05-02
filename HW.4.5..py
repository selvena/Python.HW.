from functools import reduce
def my_list(el, el_2):
    return el * el_2
result = [el for el in range(100, 1001, 2)]
print(f"Список четных значений {result},\nРезультат произведения {reduce(my_list, result)}")


