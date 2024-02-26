
def interactiveLoop():
    ans = "yes"
    _sum = 0
    count = 0
    while ans[0] == "y":
        num = eval(input("give me the number: "))
        _sum = _sum + num
        count = count + 1
        ans = input("Do you have any more numbers (yes/no): ")
    print("AVG is ", _sum/count)


def sentinelLoop():
    _sums = 0
    counts = 0
    nums = eval(input("give me the positive number: "))
    while nums >= 0:
        _sums = _sums + nums
        counts = counts + 1
        nums = eval(input("give me the positive number: "))
    print("AVG is ", _sums/counts)


def sentinelLoop2():
    _sums = 0
    counts = 0
    nums = input("give me the positive number: ")
    while nums != "":
        _sums = _sums + eval(nums)
        counts = counts + 1
        nums = input("give me the positive number: ")
    print("AVG is ", _sums/counts)




def main():
    print("Advance Loop")
    for i in range(10):
        print("Hello World!")


main()
interactiveLoop()
sentinelLoop()
sentinelLoop2()