with open("EX.2.txt", 'r', encoding="utf-8") as f:
    text = [f"{line}. {count.strip()} - {len(count.split())} слов" for line, count in enumerate(f, 1)]
    print(*text, f"Всего строк - {len(text)}.", sep="\n")