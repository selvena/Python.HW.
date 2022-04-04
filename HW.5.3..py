# def f_3():
#     summa = {}
#     try:
#         with open("EX.3.txt", 'r', encoding="utf-8") as file_3:
#             for line in file_3:
#                 summa[line.split()[0]] = float(line.split()[1])
#         print("Оклад менее 20000 имеют: ")
#         for name, sum in summa.items():
#             if sum < 20000:
#                 print(name)
#         print(f"Средняя величина дохода: {sum(summa.values()) / len(summa)}")
#     except EOFError:
#         print("Расчеты ")

with open("EX.3.txt", 'r', encoding="utf-8") as file_3:
    empl = {line.split()[0]: float(line.split()[1]) for line in  file_3}
    print(f"Сотрудники с окладом менее 20000: {[s[0] for s in empl.items() if s[1] < 20000]}\n"
          f"Средний оклад по организации: {round(sum(empl.values()) / len(empl), 3)}")