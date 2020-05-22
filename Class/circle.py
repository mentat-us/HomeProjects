import math
class Circle:
    def __init__(self, r=0):
        self.__radius = r
    def get_area(self):
        area = math.pi * pow(self.__radius, 2);
        return area
    #getter method
    def get_radius(self):
        return self.__radius

    #setter method
    def set_radius(self, radius):
        self.__radius = radius


#############################3

def get_area(radius):
    area = math.pi * pow(radius, 2);
    return area

print(get_area(0))


circle_0 = Circle()
area_0 = circle_0.get_area()
print(circle_0.get_radius() ," yarıçaplı çemberin alanı: ", area_0)


circle_1 = Circle(3)
circle_1.set_radius(5)
area_1 = circle_1.get_area()
print("Circle 1 area:", area_1)

circle_2 = Circle(5)
area_2 = circle_2.get_area()
print("Circle 2 area:", area_2)