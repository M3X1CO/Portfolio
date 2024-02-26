amount = float(input('Money >> '))
years = int(input('Number of years >> '))
rate = float(input('Interest rate (%) >> '))
fv = amount * (1 + rate/100) ** years

print('\nMoney in the future: %.2f.' %fv)

