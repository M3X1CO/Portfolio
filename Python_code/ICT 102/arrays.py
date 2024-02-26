def input_array():
    number = []

    


def main():
    print("Data Collection -Array.... ")
    x = 100
    y = 10
    item = [100, 200, "RSU", True, 3.4, "B+", 45.6]
    score = [56, 64, 100, 99, 10]

    print(item[1])
    print(item[2] + str(score[2]))
    print(item[5]*10)
    print(item[2:5])

    for i in range(5):
        if score[i] >= 50:
            print(score[i])
            print("you passs...")
        else:
            print(score[i])
            print("unlucky")

    for j in range(len(item)):
        print(item[j])




if __name__ == "__main__":
    main()