def interpreter():
    expression = input('Enter an arithmetic expression in the format "x y z": ')
    x, operator, z = expression.split()

    x = int(x)
    z = int(z)

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z != 0:
            result = x / z
        else:
            print('Error: Division by zero is not allowed.')
            return
    else:
        print('Error: Invalid operator.')
        return

    print(f'Result: {result:.1f}')

interpreter()
