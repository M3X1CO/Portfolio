def check_if_prime(q):
    if q <= 1:
        return False
    if q <= 3:
        return True
    if q % 2 == 0 or q % 3 == 0:
        return False
    i = 5
    while i * i <= q:
        if q % i == 0 or q % (i + 2) == 0:
            return False
        i += 6
    return True


def main():
    q = int(input('Enter a number to check if Prime: '))
    while not check_if_prime(q):
        print(q, 'is not Prime')
        q = q + 1
        check_if_prime(q)

    else:
        print(q, 'is Prime')

if __name__ == "__main__":
    main()
