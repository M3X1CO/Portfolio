import math

a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

d=(b**2) - (4*a*c)

root1=(-b+math.sqrt(d))/(2*a)
root2=(-b-math.sqrt(d))/(2*a)

print(root1,root2)
