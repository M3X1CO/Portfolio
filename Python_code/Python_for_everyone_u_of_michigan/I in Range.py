sum = 0

for i in range(1, 51):
    print(i, end='')
    sum += i
    if i % 10 == 0:
        print('sum =', sum)
        sum = 0

sum = 0
i = 1

while i <= 50:
    print(i, end='')
    sum += i
    if i % 10 == 0:
        print('sum =', sum)
        sum = 0
    i = i+1
