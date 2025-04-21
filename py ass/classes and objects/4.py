

class Shape:
    def __init__(self, shape_type, *dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def perimeter(self):
        if self.shape_type == "circle":
            return 2 * 3.14 * self.dimensions[0]
        elif self.shape_type == "rectangle":
            return 2 * (self.dimensions[0] + self.dimensions[1])
        elif self.shape_type == "square":
            return 4 * self.dimensions[0]
        else:
            return "Shape not recognized"

    def area(self):
        if self.shape_type == "circle":
            return 3.14 * (self.dimensions[0] ** 2)
        elif self.shape_type == "rectangle":
            return self.dimensions[0] * self.dimensions[1]
        elif self.shape_type == "square":
            return self.dimensions[0] ** 2
        else:
            return "Shape not recognized"
        

shape1 = Shape("circle", 5)
print(f"Circle - Perimeter: {shape1.perimeter()}, Area: {shape1.area()}")


shape2 = Shape("rectangle", 4, 6)
print(f"Rectangle - Perimeter: {shape2.perimeter()}, Area: {shape2.area()}")


shape3 = Shape("square", 3)
print(f"Square - Perimeter: {shape3.perimeter()}, Area: {shape3.area()}")


shape4 = Shape("triangle", 3, 4, 5)
print(f"Triangle - Perimeter: {shape4.perimeter()}, Area: {shape4.area()}")


