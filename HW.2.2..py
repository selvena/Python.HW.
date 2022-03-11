el_1 = input('Ведите список значений:  ').split()
list(el_1)
el_2 = []
for i in range(1, len(el_1), 2):
    el_1[i - 1], el_1[i] = el_1[i], el_1[i - 1]
print(' '.join([str(i) for i in el_1]))



