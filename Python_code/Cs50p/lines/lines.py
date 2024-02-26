import sys

def main():
    # check cmd line args
    check_command_line_arg()
    # try to open file
    try:
        file = open(sys.argv[1])
        lines = file.readlines()
        
    # does file exist
    except FileNotFoundError:
        sys.exit("File does not exist")
    # loop through lines and check for empty or #
    count_lines = 0
    for line in lines:
        if check_line(line) == False:
            count_lines += 1
    print(count_lines)

# fun check cmd line args
def check_command_line_arg():
    # check how many elements in the cmd line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguements")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguements")
    # check if it is a python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def check_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()