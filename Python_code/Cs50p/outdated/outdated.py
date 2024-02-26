def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Ask for a date until a valid one is given
    while True:
        date_str = input("Enter a date (MM/DD/YYYY or Month DD, YYYY): ").strip()

        # Check for the two specific formats
        if '/' in date_str:
            parts = date_str.split('/')
            if len(parts) != 3 or not parts[0].isdigit():
                print("Invalid format, please try again.")
                continue
            month, day, year = parts
            month = int(month)  # Convert month to integer
        elif ',' in date_str:
            month_day, year = date_str.split(',', 1)  # Split date into two parts
            parts = month_day.split()  # Split the first part into month and day
            if len(parts) != 2 or not year.strip().isdigit():
                print("Invalid format, please try again.")
                continue
            month, day = parts
            # Make month case-insensitive and convert from name to number
            month = month.capitalize()
            if month in months:
                month = months.index(month) + 1
            else:
                print("Invalid month, please try again.")
                continue
        else:
            print("Invalid format, please try again.")
            continue

        # Ensure month, day, year are numbers and within valid ranges
        if not (day.isdigit() and year.strip().isdigit() and
                1 <= month <= 12 and 1 <= int(day) <= 31 and int(year) >= 0):
            print("Invalid date, please try again.")
        else:
            # Print the date in the new format
            print(f"{int(year):04}-{month:02}-{int(day):02}")
            break

# Run the main function
if __name__ == "__main__":
    main()
