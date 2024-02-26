import math

x = float(input('Enter Number for X >>'))
y = float(input('Enter Number for Y >>'))

f = 3 / 7
g = 5 / 11
log = math.log(10,(x))

a = x**3
b = x**2

c = f * b
d = g * a

y = 2 - x + c - d + log

print(y)