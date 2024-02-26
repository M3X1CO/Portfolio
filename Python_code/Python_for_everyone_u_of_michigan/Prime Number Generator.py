for q in range(1, 10001):
    for k in range(2, q+1):
        if q % k == 0:
            break
    if q == 1:
        print('q = 1 is not Prime')
    elif k == q:
        print(q,'is prime')
    else:
        print(q, '=', k, 'x', q//k)
        print(q, 'is not Prime')