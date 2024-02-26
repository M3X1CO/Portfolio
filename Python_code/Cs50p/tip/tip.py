def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(change):
    change = change.replace('$', '')
    amount = float(change)
    return amount

def percent_to_float(percent):
    percent = percent.replace('%', '')
    percentage = float(percent) / 100
    return percentage

main()