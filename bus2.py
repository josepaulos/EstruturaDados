class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
class moto(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=2):
        return super().seating_capacity(capacity=2)        

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())
 
moto = moto("cd 500", 200, 32)
print(School_bus.seating_capacity())
 