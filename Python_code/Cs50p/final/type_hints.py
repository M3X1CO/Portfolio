def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ")
meow(number)

# run this code with
# mypy type_hints.py
