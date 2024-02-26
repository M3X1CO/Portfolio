def main():
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = map(int, fuel.split('/'))
            result = convert_fuel(x, y)
            if isinstance(result, int):  # Check if result is a number
                print(f"{result}%")  # Add a "%" sign to the number
            else:
                print(result)  # If not a number, just print the result
            break

        except(ValueError, ZeroDivisionError, Exception):
            pass

def convert_fuel(x, y):
    ratio = round(x / y * 100)
    if ratio <= 1:
        return("E")
    elif 99 <= ratio <= 100:
        return("F")
    elif ratio > 100:
        raise Exception
    elif 1 < ratio < 99:
        return ratio
    else:
        raise Exception

if __name__ == "__main__":
    main()