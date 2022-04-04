with open("my_fail.txt", 'w', encoding="utf-8") as f:
    while True:
        text = input("Для выхода введите пустую строку.\nВведите данные для записи:")
        if not text:
            break
        print(text, file=f)
