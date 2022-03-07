time = int (input("Введите время в секундах: "))
print(f'{(time // 3600):02}:{int((time % 3600) / 60):02}:{int(time % 3600) % 60:02}')
