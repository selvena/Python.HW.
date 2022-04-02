from itertools import count
from math import factorial
def fact_n():
    for el in count(1):
        yield factorial(el)
g = 0
for n in fact_n():
    if g > 15:
        break
    else:
        g += 1
        print(n)





