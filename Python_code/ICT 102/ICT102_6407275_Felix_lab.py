import random
import sys


def main():
    name = input("Enter your name: ")
    name = name.lower().capitalize()
    balance = 100000
    is_existing(name)

    while True:
        selection = options()
        balance = get_options(selection, balance)


def options():
    try:
        option = int(input("1. Withdraw\n 2. Deposit\n 3. Electronic Fund Transfer(EFT)\n 4. Check Balance\n 5. Quit Program\n"))
        return option
    except (ValueError, UnboundLocalError):
        print("Please pick an available option")


def is_existing(name):
    accounts = []
    account_number_generator = random.randint(10 ** 9, (10 ** 10) - 1)
    new_account = {'name': name, 'account_number': account_number_generator}
    accounts.append(new_account)
    print(f"Welcome {accounts[0]['name']}, your account number is {accounts[0]['account_number']}")


def get_options(selection, balance):
    if selection == 1:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw >= 0:
            if withdraw <= balance:
                balance = balance - withdraw
                print(f"Your remaining balance is: {balance}")
            else:
                print(f"Withdraw is greater than your balance of {balance}.")
        else:
            print("Please withdraw a positive amount")
    elif selection == 2:
        try:
            deposit = int(input("Enter amount to deposit: "))
            if deposit >= 0:
                balance = balance + deposit
                print(f"Your remaining balance is: {balance}")
            else:
                print("Please deposit a positive amount")
        except ValueError:
            print("Please enter a correct value to deposit")
    elif selection == 3:
        try:
            eft = int(input("Enter an account number: "))
            while True:
                if len(str(eft)) == 10:
                    send = int(input("How much would you like to send? "))
                    if 0 <= send <= balance:
                        confirm = input(f"Confirm transfer of {send} to {eft} y or n\n")
                        if confirm == 'y':
                            print(f"{send} successfully sent to {eft}")
                            balance = balance - send
                            break
                        else:
                            print("Transaction stopped")
                            break
                    else:
                        print("Please check the amount you would like to send")
                else:
                    print("Enter a 10 digit account number.")
        except ValueError:
            print("Please enter a correct value")
    elif selection == 4:
        print(f"Your balance is {balance}")
    else:
        sys.exit()

    return balance


if __name__ == "__main__":
    main()
