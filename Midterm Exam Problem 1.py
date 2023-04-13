class circle:
    def __init__ (self,diameter):
        self.diameter=diameter
        self.pi=3.14
    def perimeter(self):
        return (self.pi*self.diameter)
    def area(self):
        return (self.pi*self.diameter**2)/4
    def display(self):
        return print("The Perimeter of the Circle is: ", self.perimeter(), "The Area of the Circle is: ", self.area())

CircleA=circle(float(input("Insert a value of Diameter: ")))
CircleA.display()