from itertools import count
for el in count(3):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle
c = 0
for el in cycle("qwertyuiop"):
    if c > 15:
        break
    print(el)
    c += 1

