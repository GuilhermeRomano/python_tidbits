class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Started, let's ride!")
    def stop(self):
        self.speed = 0
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")

class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        trunk_open = True
    def close_trunk(self):
        trunk_open = False


car1 = Car(started=True, speed=50)
