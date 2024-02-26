import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    # open the image
    try:
        imageFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # open shirt
    try:
        shirtFile = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # get the size of the shirt
    size = shirtFile.size
    # resize the mupptes image to fit the shirt
    muppet = ImageOps.fit(imageFile, size)
    # paste shirt on muppets
    muppet.paste(shirtFile, shirtFile)
    # create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
    # check how many args in cmd line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguements")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    #print(file1[1])
    #print(file2[1])
    # check if its is an image file jpg jpeg or png
    #print(check_extension(file1[1]))
    #print(check_extension(file2[1]))
    if check_extension(file1[1]) == False:
        sys.exit("Invalid Input")
    if check_extension(file2[1]) == False:
        sys.exit("Invalid Output")
    # check if extensions in both files are the same...?
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def check_extension(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()
