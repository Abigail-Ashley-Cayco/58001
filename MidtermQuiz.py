class DistanceConverter:
    def __init__(self):
        self.__meter = 0.0

    def set_meter(self, meter):
        self.__meter = meter

    def __to_centimeters(self):
        return self.__meter * 100

    def __to_kilometers(self):
        return self.__meter / 1000

    def __to_inches(self):
        return self.__meter * 39.37

    def convert_to_all(self):
        centimeters = self.__to_centimeters()
        kilometers = self.__to_kilometers()
        inches = self.__to_inches()
        return (centimeters, kilometers, inches)

    def set_centimeters(self, centimeters):
        self.__meter = centimeters / 100

    def set_kilometers(self, kilometers):
        self.__meter = kilometers * 1000

    def set_inches(self, inches):
        self.__meter = inches / 39.37

distance_converter = DistanceConverter()
distance_converter.set_meter(float(input("Enter distance in meters: ")))

centimeters, kilometers, inches = distance_converter.convert_to_all()

print(
    f"{distance_converter._DistanceConverter__meter} meters is equal to {centimeters} centimeters, {kilometers} kilometers, and {inches} inches")


distance_converter.set_centimeters(float(input("Enter distance in centimeters: ")))

distance_converter.set_meter(distance_converter._DistanceConverter__to_centimeters() / 100)
kilometers, inches = dsitance_converter.convert_to_all()[1:]

print(
    f"{distance_converter._DistanceConverter__meter} centimeters is equal to {distance_converter._DistanceConverter__meter:.6f} meters, {kilometers:.6f} kilometers, and {inches:.6f} inches")

distance_converter.set_kilometers(float(input("Enter distance in kilometers: ")))

distance_converter.set_meter(distance_converter._DistanceConverter__to_kilometers() * 1000)
centimeters, inches = distance_converter.convert_to_all()[:1] + distance_converter.convert_to_all()[2:]

print(
    f"{distance_converter._DistanceConverter__meter} kilometers is equal to {distance_converter._DistanceConverter__meter:.6f} meters, {centimeters:.6f} centimeters, and {inches:.6f} inches")

distance_converter.set_inches(float(input("Enter distance in inches: ")))

distance_converter.set_meter(distance_converter._DistanceConverter__to_inches() / 39.37)
centimeters, kilometers = distance_converter.convert_to_all()[:1] + distance_converter.convert_to_all()[1:2]

print(
    f"{distance_converter._DistanceConverter__meter} inches is equal to {distance_converter._DistanceConverter__meter:.6f} meters, {centimeters:.6f} centimeters, and {kilometers:.6f} kilometers")