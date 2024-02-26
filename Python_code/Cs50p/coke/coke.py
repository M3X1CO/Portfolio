def main():
    total = 0
    amount_due = 50
    print(f"Amount Due: {amount_due}")
    while total < 50:
        coin = int(input("Insert a coin: "))
        if coin in [5, 10, 25]:
            total += coin
            amount_due = 50 - total
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
            else:
                print(f"Change Owed: {abs(amount_due)}")
        else:
            print(f"Invalid coin. Amount Due: {amount_due}")

if __name__ == "__main__":
    main()
