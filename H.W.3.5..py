s = 0
try:
    while True:
       for n in map(int, input("Введите список чисел, разделенных пробелом: ").split()):
           s += n
    print(s)
except ValueError as er:
    print(s)