month_key = int(input('Введите порядковый номер месяца (1-12): '))

while month_key <= 0 or month_key > 12:
            print('Вы ввели не корректное значение. Ведите число от 1 до 12')
            month_key = int(input('Введите порядковый номер месяца (1-12): '))
month_dict = {12:'Декабрь', 1:'Январь', 2:'Февраль', 3:'Март', 4:'Апрель', 5:'Май', 6:'Июнь', 7:'Июль',
                8:'Август', 9:'Сентября', 10:'Октябрь', 11:'Ноябрь'}
seasons_dict = {12:'Зима',1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна',
                6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень'}

print(month_key, "месяц ", month_dict.setdefault(month_key), "сезона",
      seasons_dict.setdefault(month_key) )