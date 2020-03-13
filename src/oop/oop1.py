# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: # No Base Class
    def __init__(self, name):
        self.name = namm


class GroundVehicle(Vehicle): # Base is Vehicle
    def __init__(self, name, ground_speed):
        super().__init__(name)
        self.ground_speed = ground_speed


class Car(GroundVehicle): # Base is GroundVehicle
    def __init__(self, name, ground_speed, license_plate):
        super().__init__(name, ground_speed)
        self.license_plate = license_plate


class Motorcycle(GroundVehicle):
    def __init__(self, name, ground_speed, width_of_handlebars):
        super().__init__(name, ground_speed)
        self.width_of_handlebars = width_of_handlebars


class FlightVehicle(Vehicle): # Base is Vehicle
    def __init__(self, name, air_speed):
        super().__init__(name)
        self.air_speed = air_speed

class Airplane(FlightVehicle): # Base is FlightVehicle
    def __init__(self, name, air_speed, prop_size):
        super().__init__(name, air_speed)
        self.prop_size = prop_size


class Starship(FlightVehicle): # Base is FlightVehicle
    def __init__(self, name, air_speed, max_warp):
        super().__init__(name, air_speed)
        self.max_warp = max_warp