from abc import ABC, abstractmethod
class Polygon(ABC):
    def get_dimensions(self):
        pass
    def calculate_area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_dimensions(self):
        return f"Length: {self.length}\nBreadth: {self.breadth}"

    def calculate_area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_dimensions(self):
        return f"Base: {self.base}\nHeight: {self.height}"

    def calculate_area(self):
        return 0.5 * self.base * self.height


length_rect = float(input("Enter length of rectangle: "))
breadth_rect = float(input("Enter breadth of rectangle: "))

base_tri = float(input("Enter base of triangle: "))
height_tri = float(input("Enter height of triangle: "))

rectangle = Rectangle(length_rect, breadth_rect)
triangle = Triangle(base_tri, height_tri)

print("\nRectangle:")
print(rectangle.get_dimensions())
print(f"Area: {rectangle.calculate_area()}")

print("\nTriangle:")
print(triangle.get_dimensions())
print(f"Area: {triangle.calculate_area()}")
