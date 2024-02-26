radius = float(input('Radius:'))
height = float(input('Height:'))
surface=2*3.14159*radius*height+2*3.14159*radius**2
circumference=2*3.14159*radius
volume=3.14159*radius**2*height
print(f'Radius of the circle is {radius} and surface of the circle is \
{surface:.2f} sq. m. The Circumference of the circle is {circumference:.3f}m. \
Volume of the circle is {volume:.4f} meters cubed')
