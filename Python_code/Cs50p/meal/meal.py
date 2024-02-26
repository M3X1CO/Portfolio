def main():
    time = input('Enter a time in 24-hour format (#:## or ##:##): ')
    time_in_hours = convert(time)

    if 7 <= time_in_hours <= 8:
        print("breakfast time")
    elif 12 <= time_in_hours <= 13:
        print("lunch time")
    elif 18 <= time_in_hours <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = map(int, time.split(':'))
    return hours + minutes / 60


if __name__ == "__main__":
    main()
