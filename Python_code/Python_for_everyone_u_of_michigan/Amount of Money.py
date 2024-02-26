import math

pay = float(input('Amount of Money>>'))
remain = 0
b1000 = pay // 1000
remain = pay % 1000
b500 = pay // 500
remain = pay % 500
b100 = pay // 100
remain = pay % 100
b50 = pay // 50
remain = pay % 50
b10 = pay // 10
remain = pay % 10
b1 = pay // 1
remain = pay % 1

print(remain)
