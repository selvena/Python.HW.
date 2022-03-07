start = float(input("Введите результаты пробежки первого дня (км): "))
finish = float(input("Введите желаемые результаты пробежки (км): "))
day = 1
print(day, '-й день: ', "%.2f" % start)
while True:
    day = day + 1
    start = (start / 100 * 10) + start
    if start >= (finish + (start / 100 * 10)):
        break
    print(day, '-й день: ', "%.2f" % start)


