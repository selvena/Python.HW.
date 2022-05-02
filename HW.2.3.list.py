month = int(input('Введите порядковый номер месяца (1-12): '))
while month <= 0 or month > 12:
            print('Вы ввели не корректное значение. Ведите число от 1 до 12')
            month = int(input('Введите порядковый номер месяца (1-12): '))
seasons_List = ['Зима', 'Весна', 'Лето', 'Осень']
if month <=2 and month >0:
    print(month, 'месяц относится к сезону ', (seasons_List[0]))
elif month ==12:
    print(month, 'месяц относится к сезону ', seasons_List[0])
elif month <=5  and month >2:
    print(month, 'месяц относится к сезону ', seasons_List[1])
elif month <= 8 and month > 5:
    print(month, 'месяц относится к сезону ', seasons_List[2])
elif month <= 11 and month > 8:
    print(month, 'месяц относится к сезону ', seasons_List[3])

