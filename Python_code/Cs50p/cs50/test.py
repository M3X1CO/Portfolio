def main():
    math = input("Please enter an equation in form 'x y z': ")
    x, operator, z = math.split()

    x = int(x)
    z = int(z)

    result = calculate(x, operator, z)
    if result is not None:
        print(f'Result: {result:.1f}')

def calculate(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        if z != 0:
            return x / z
        else:
            print('Error: Division by zero is not allowed.')
            return None
    else:
        print('Error: Invalid operator')
        return None

if __name__ == "__main__":
    main()