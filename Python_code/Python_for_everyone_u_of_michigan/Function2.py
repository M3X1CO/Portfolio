import math

a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

root1 = (-b+math.sqrt(b*b-4*a*c))/2*a
root2 = (-b-math.sqrt(b*b-4*a*c))/2*a

print(root1,root2)