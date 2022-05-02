from sys import argv
def wages():
    try:
        productivity, bet, prize = map(float, argv[1:])
        print(f"Выработка в часах: {productivity}, Ставка в час: {bet} , Премия: {prize} , Заработная плата: {(productivity * bet) + prize}")
    except ValueError:
        print("Указаны не все параметры для расчета.")
wages()

