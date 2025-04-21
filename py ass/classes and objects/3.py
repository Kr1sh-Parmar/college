

class Solid:
    def __init__(self, name, radius=None, height=None):
        self.name = name
        self.radius = radius
        self.height = height

    def surface_area(self):
        if self.name == "sphere":
            return 4 * 3.14 * (self.radius ** 2)
        elif self.name == "cylinder":
            return 2 * 3.14 * self.radius * (self.radius + self.height)
        elif self.name == "cone":
            return 3.14 * self.radius * (self.radius + (self.height ** 2 + self.radius ** 2) ** 0.5)
        else:
            return "Unknown solid"

    def volume(self):
        if self.name == "sphere":
            return (4 / 3) * 3.14 * (self.radius ** 3)
        elif self.name == "cylinder":
            return 3.14 * (self.radius ** 2) * self.height
        elif self.name == "cone":
            return (1 / 3) * 3.14 * (self.radius ** 2) * self.height
        else:
            return "Unknown solid"
        

solid1 = Solid("sphere", radius=5)
solid2 = Solid("cylinder", radius=3, height=7)
solid3 = Solid("cone", radius=4, height=9)

print(f"Surface area of {solid1.name}: {solid1.surface_area()}")
print(f"Volume of {solid1.name}: {solid1.volume()}")
print(f"Surface area of {solid2.name}: {solid2.surface_area()}")
print(f"Volume of {solid2.name}: {solid2.volume()}")
print(f"Surface area of {solid3.name}: {solid3.surface_area()}")
print(f"Volume of {solid3.name}: {solid3.volume()}")


