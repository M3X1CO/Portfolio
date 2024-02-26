def main():
    grocery_dict = {}

    while True:
        try:
            item = input("").lower()
        except EOFError:
            break

        if item in grocery_dict:
            grocery_dict[item] += 1
        else:
            grocery_dict[item] = 1

    for item, count in sorted(grocery_dict.items()):
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()