import sys
import csv

def main():
    # check cmd line args
    check_command_line_arg()
    # create list
    output = []
    # try to open file
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                # create first name last name
                output.append({'first': split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
        # print(output)

    # open file or does not exist
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    # write file to csv
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})
            # print(f'{row["first"]}, {row["last"]}, {row["house"]}')

def check_command_line_arg():
    # check how many elements are in cmd line
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguements")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguements")
    # check if it is a csv file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
if __name__ == "__main__":
    main()
