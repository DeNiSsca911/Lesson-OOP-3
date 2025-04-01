class Engine():
    def start(self):
        print("двигатель запущен")

    def stop(self):
        print("двигатель остановлен")

class Car():
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

my_Car = Car()
my_Car.start()
my_Car.stop()