menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total_cost = 0.0

    while True:
        try:
            item = input("Item: ").lower().title()
            if item in menu:
                total_cost += menu[item]
                print(f"Total Cost: ${total_cost:.2f}")

        except EOFError:
            break


if __name__ == "__main__":
    main()