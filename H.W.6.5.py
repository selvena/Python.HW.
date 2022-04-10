class Stationery:
    def __init__(self, title="Твори! Проявляйся!"):
        self.title = title

    def draw(self):
        print(f"Рисуй! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Возьми карандаш {self.title}!")

class Pencil(Stationery):
    def draw(self):
        print(f"Возьми ручку {self.title}!")

class Marker(Stationery):
    def draw(self):
        print(f"Возьми маркер {self.title}!")

stat = Stationery()
pen = Pen("Красный")
pencil = Pencil("Синюю")
marker = Marker("Желтый")

chancellery = [stat, pen, pencil, marker]

for c in chancellery:
    c.draw()



