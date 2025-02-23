class Car:
    def start(self):
        print("whroom")

class PassangerCar(Car):    # Uses default start logic
    pass

class Truck(Car):           # Overrides start logic
    def start(self):
        print("WHROOM")

pc = PassangerCar()
pc.start()          # Expected: whroom
t = Truck()
t.start()           # Expected: WHROOM