# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Subclass Car overrides move()
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

# Subclass Bicycle overrides move()
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Demonstration of polymorphism
def show_movement(vehicle):
    vehicle.move()


# Example usage
car = Car()
bicycle = Bicycle()

# Calling move() directly
car.move()
bicycle.move()

print("\n--- Using polymorphism ---")
# Passing different objects to the same function
show_movement(car)
show_movement(bicycle)
