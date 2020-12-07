def number(x):
    n = 10
    for i in range(0, x):
        for j in range(0, i + 1):
            print(n, end=' ')
            n = n + 10
        print('\r')


x = 5
number(x)
