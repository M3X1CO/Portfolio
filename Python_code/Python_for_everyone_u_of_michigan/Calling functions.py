import math

def print_twice(value):
    print(value)
    print(value)


print_twice('Spam')
print_twice(math.pi)
print_twice('math.pi')

def print_twice(value):
    print(value)
    print(value)


def cat_twice(part1,part2):
    cat = part1 + part2
    print_twice(cat)


cat_twice('CPE252','RSU')
cat_twice(2 , 9)
print_twice('Spam')
print_twice(42)
print_twice(math.pi)
print_twice('Spam '*4)