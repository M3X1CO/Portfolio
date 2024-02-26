import math

def area(radius):
    a = math.pi * radius**2
    return a

r = float(input('radius : '))
circle_area = area(r)
print(circle_area)