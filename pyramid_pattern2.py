def pypart(n):
    myList = []
    for i in range(0, n + 1):
        myList.append('* ' * i)
    print('\n'.join(myList))


pypart(n=5)
