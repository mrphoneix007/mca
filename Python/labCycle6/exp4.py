class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

def compare_rectangles(rect1, rect2):
    area1 = rect1.area()
    area2 = rect2.area()

    if area1 > area2:
        return "Rectangle 1 has a greater area."
    elif area1 < area2:
        return "Rectangle 2 has a greater area."
    else:
        return "Both rectangles have the same area."

length_rect1 = float(input("Enter length of rectangle 1: "))
breadth_rect1 = float(input("Enter breadth of rectangle 1: "))

length_rect2 = float(input("Enter length of rectangle 2: "))
breadth_rect2 = float(input("Enter breadth of rectangle 2: "))

rectangle1 = Rectangle(length_rect1, breadth_rect1)
rectangle2 = Rectangle(length_rect2, breadth_rect2)

area_rect1 = rectangle1.area()
perimeter_rect1 = rectangle1.perimeter()

area_rect2 = rectangle2.area()
perimeter_rect2 = rectangle2.perimeter()

print("\nRectangle 1:")
print(f"Area: {area_rect1}")
print(f"Perimeter: {perimeter_rect1}")

print("\nRectangle 2:")
print(f"Area: {area_rect2}")
print(f"Perimeter: {perimeter_rect2}")

print(compare_rectangles(rectangle1, rectangle2))
