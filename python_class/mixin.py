class AdditionalMixin:
    def connect_to_wifi(self):
        print("connect to wifi!")

    def pley_music(self):
        print("play music")


class ThermometerMixin:
    def check_thermometer(self):
        print("check thermometer!")


class Vehicle:
    def move(self):
        pass


class Car(Vehicle, AdditionalMixin):
    pass


class AirPlane(Vehicle,AdditionalMixin,ThermometerMixin):
    pass


class MotorCycle(Vehicle):
    pass
