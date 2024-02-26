import sys
import csv
from tabulate import tabulate

def main():
    check_command_line_arg()
    # create variable to store table data
    table = []
    # try to open file
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
    # if can't open file sys exit does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # print the table
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

def check_command_line_arg():
    # check how many args in the cmd line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    # check if its a csv file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()