import math

x1 = float(input('Input x1 >>'))
x2 = float(input('Input x2 >>'))
y1 = float(input('Input y1 >>'))
y2 = float(input('Input y2 >>'))

a = x2 - x1
b = y2 - y1

c = a**2
d = b**2
e = c + d

f = e**.5

Diameter = f
Radius = Diameter / 2

Aoc = math.pi * Radius**2

print(Aoc)