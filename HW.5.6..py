hours = {}
with open("EX.6.txt", encoding="utf-8") as hs:
    for line in hs:
        name, stats = line.split(':')
        name_sum = sum(map(int, "".join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        hours[name] = name_sum
print(f"{hours}")

