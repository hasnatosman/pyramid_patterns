# function to demonstrate printing pattern

def pypart(n):

    # outer loop to handle numbers of rows.
    for i in range(0, n):

        # inner loop to handle numbers of column and printing the stars.
        for j in range(0, i+1):
            print('*', end=' ')
        print('\r')


n = 6
pypart(n)