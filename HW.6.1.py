from time import sleep

class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("Светофор красный")
            sleep(7)
            print("Светофор желтый")
            sleep(2)
            print("Светофор зеленый")
            sleep(7)
            print("Светофор желтый")
            sleep(2)
trafficlight = TrafficLight()
trafficlight.running()