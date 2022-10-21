class Vehicle:
    # class attribute
    color = 'white'

    def __init__(self, max_speed, milage):
        self.capacity = None
        self.max_speed = max_speed
        self.mileage = milage

    def seating_capacity(self, capacity=50):
        self.capacity = capacity
        return f"Seating capacity {capacity}"

    def fare(self):
        pass


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def fare(self):
        fare = self.capacity * 100
        total_fare = (fare * 0.1) + fare
        return total_fare


class Gadget:
    pass


bus = Bus(70, 1200)
print(bus.seating_capacity())
print(bus.fare())
print(isinstance(bus, Vehicle))
print(isinstance(bus, Bus))
print(isinstance(bus, Gadget))
