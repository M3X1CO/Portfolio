def meow(n: int) -> str: #None can be used in str place
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

# run this code with
# mypy type_hints.py
