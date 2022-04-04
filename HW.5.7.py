import json

with open("EX.7.json", "w", encoding="utf-8") as new_f:
    with open("EX.7.txt", encoding="utf-8") as new_f_2:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in new_f_2}
        result = [profit, {"Средняя прибыль": round(sum([int(i) for i in profit.values() if int(i) > 0]), len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, new_f, ensure_ascii=False, indent=4)