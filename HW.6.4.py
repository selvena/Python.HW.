from random import choice

class Car:
    direction = ["На лево", "На право"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f"Новая машина {n} цвет {c}.\ Машина полиции? {p}")

    def go(self):
        print(f"{self.name}: Машина поехала.")

    def stop(self):
        print(f"{self.name}: Машина остановилась.")

    def turn(self):
        print(f"{self.name}: Машина повернула. {choice(self.direction)}.")

    def show_speed(self):
        return f"{self.name}: Скорость машины: {self.speed}."

class TownCar(Car):
    def show_speed(self):
        return f"{self.name}: Скорость машины: {self.speed}. Уменьшите скорость!" if self.speed > 60 else super().show_speed()

class WorkCar(Car):
    def show_speed(self):
        return f"{self.name}: Скорость машины: {self.speed}. Уменьшите скорость!" if self.speed > 40 else super().show_speed()

class SportCar(Car):
    pass

class PoliceCar(Car):

    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)

work_car = WorkCar('Каблук', 'Синий', 40)
town_car = TownCar('Жук, ниссан', 'Красная', 60)
sport_car = SportCar('Спортивная машина', 'Пурпурный', 110)
police_car = PoliceCar('Полицейская машина', 'Белая с синим', 90)

list_of_cars = [work_car, town_car, sport_car, police_car]

for f in list_of_cars:
    f.go()
    print(f.show_speed())
    f.turn()
    f.stop()
    print()