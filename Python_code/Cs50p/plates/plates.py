def main():
    plate = input("Plate: ")
    plate = plate.upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) > 6:
        return False
    elif plate[0] == 'O' or not (plate[0].isalpha() and plate[1].isalpha()):
        return False
    for char in plate:
        if char.isdigit():
            if char.isalpha():
                return False
            else:
                return True
    else:
        return False



main()