def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >=0:
            return "Внесите корректные данные. "
        else:
            return x**y
    except ValueError:
        return "Внесите корректные данные"
a = input('Введите действительное положительное число: ')
b = input('Ведите число меньше 0 ')
print(my_func(a, b))
