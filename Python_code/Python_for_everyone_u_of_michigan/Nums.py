NUMS = [20, 60, 99, 55, 34, 48, 73, 80]
count_odd = 0
for n in NUMS:
    if n % 2 != 0:
        print(n, end=' ')
        count_odd += 1
print("Total odd numbers:", count_odd)
