# 🧩 MINI PROJECT: VEHICLE RENTAL SYSTEM (Abstraction)

# Goal:

# Abstract Base Class: Vehicle
# Abstract Methods: rent(), return_vehicle()

# Child Classes: Car, Bike, Truck

# Requirements:
# Each child class must implement rent() and return_vehicle()
# Each child prints a unique message for renting and returning

# Example:
# vehicles = [Car(), Bike(), Truck()]

# for v in vehicles:
#     v.rent()
#     v.return_vehicle()

# 🎯 TASK FOR YOU
# Create an abstract class Vehicle with rent() and return_vehicle() as abstract methods
# Create Car, Bike, Truck classes that inherit from Vehicle
# Implement the methods with unique print messages for each vehicle type
# Test with a list of vehicles using a loop

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def return_vehicle(self):
        pass


class Car(Vehicle):
    def rent(self):
        print("Car has been rented!")
    
    def return_vehicle(self):
        print("Car has been returned!")


class Bike(Vehicle):
    def rent(self):
        print("Bike has been rented!")
    
    def return_vehicle(self):
        print("Bike has been returned!")


class Truck(Vehicle):
    def rent(self):
        print("Truck has been rented!")
    
    def return_vehicle(self):
        print("Truck has been returned!")


vehicle = [Car(), Bike(), Truck()]
for i, v in enumerate(vehicle):
    print(f'\nVehicle {i + 1}')
    v.rent()
    v.return_vehicle()


