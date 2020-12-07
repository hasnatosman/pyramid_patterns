def triangle(x):
    s = 2*x -2
    for i in range(0, x):
        for j in range(0, s):
            print(end=' ')
        s = s - 1
        for j in range(0, i+1):
            print('.', end=' ')
        print('\r')


x = 5
triangle(x)
