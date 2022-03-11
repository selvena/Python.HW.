texst = input('Введите предложение: ')
t2 = []
texst = texst.split()
for el, tex in enumerate(texst):
    print(el+1, tex[0:10])

