def int_func(word):
    text = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(text) else False
proposal = input('Введите слова через пробел: ').split()
for w in proposal:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')