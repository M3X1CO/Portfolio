def file_loop():
    fileName = input("What file are the numbers in?: ")
    inFile = open(fileName, 'r')
    _sum = 0.0
    count = 0
    line = inFile.readline()
    while line != "":
        print(line)
        _sum = _sum + eval(line)
        count = count + 1
        line = inFile.readline()
    print("\nThe average of the numbers is", _sum / count)


def nested_loop():
    for i in range(5):
        print("i : ", i)
        for j in range(3):
            print("\tj : ", j)
            for k in range(2):
                print("\t\tk : ", k)


def stu_score():
    no_stu = eval(input("tell me the number of students: "))
    no_sub = eval(input("tell me the number of subjects: "))
    _sum = 0
    count = 0
    for i in range(no_stu):
        print("Student " + str(i + 1) + " : ")
        for j in range(no_sub):
            score = eval(input("tell me the number of subjects " + str(j + 1) + " : "))
            _sum = _sum + score
            count = count + 1
        print("##############################################################")
        print()
    print("AVG score is ", _sum/count)


def main():
    fileName = input("What file are the numbers in?: ")
    inFile = open(fileName, 'r')
    _sum = 0.0
    count = 0
    for line in inFile.readlines():
        _sum = _sum + eval(line)
        count = count + 1
    print("\nThe average of the numbers is", _sum / count)


main()
file_loop()
nested_loop()
