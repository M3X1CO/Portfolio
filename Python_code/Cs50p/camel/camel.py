def main():
    var_name = input("Enter a variable name in camelCase: ")
    print(camel_to_snake(var_name))

def camel_to_snake(name):
    snake_case = ""
    for char in name:
        if char.isupper():
            if snake_case:
                snake_case += "_"
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

if __name__ == "__main__":
    main()