def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >=0:
            return "Внесите корректные данные. "
        else:
            degree = 1
            for _ in range(abc(y))
                degree /= x
            return degree
    except ValueError:
        return "Внесите корректные данные"
num = input('Введите действительное положительное число: ')
deg = input('Ведите число меньше 0 ')
print(my_func(num, deg))

