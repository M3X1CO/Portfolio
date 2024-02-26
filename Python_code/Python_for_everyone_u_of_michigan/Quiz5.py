a = int(input('Input Amount of Seconds >>'))

b = a // 60
h = b // 60
r = a % 60
r2 = b % 60


print(h, 'Hour(s)', r2, 'Minute(s)',  r, 'Second(s)')
