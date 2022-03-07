namber = int(input("Введите целое положительное число: "))
if namber < 0:
    print("Введите число >= 0")
max = 0
anul = 0
while namber > 0:
    anul = namber % 10
    namber = namber // 10
    if anul >= max:
        max = anul
print(max)
