import math

x = float(input('x >>'))

sinx2 = (math.sin(x / 360.0 * 2 * math.pi))**2
cosx2 = (math.cos(x / 360.0 * 2 * math.pi))**2

y = sinx2 + cosx2

print(y)
