'''
def main():
    yell(["This", "is", "CS50P"])


def yell(words):
    upper_case = []
    for word in words:
        upper_case.append(word.upper())
    print(*upper_case)


if __name__ == "__main__":
    main()
'''

'''
def main():
    yell("This", "is", "CS50P")


def yell(*words):
    upper_case = []
    for word in words:
        upper_case.append(word.upper())
    print(*upper_case)


if __name__ == "__main__":
    main()
'''


'''
# using map function
def main():
    yell(["This", "is", "CS50P"])


def yell(words):
    upper_case = map(str.upper, words)
    print(*upper_case)


if __name__ == "__main__":
    main()
'''

# list comprehension
def main():
    yell(["This", "is", "CS50P"])


def yell(words):
    upper_case = [word.upper() for word in words]
    print(*upper_case)


if __name__ == "__main__":
    main()
