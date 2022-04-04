from random import randint

with open("EX.5.new.txt", mode='w+', encoding="utf-8") as new_f_5:
    new_f_5.write(" ".join([str(randint(1, 1500)) for _ in range(100)]))
    new_f_5.seek(0)
    print(sum(map(int, new_f_5.readline().split())))