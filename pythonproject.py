def generateOddSquare(n):
    magicSquare = [[0]*n for i in range(n)]
    i = n // 2
    j = n - 1
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:
            if j == n:
                j = 0
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1

    for i in range(0, n):
        for j in range(0, n):
            print(magicSquare[i][j], end=' ')
        print()


def generateDoublyEvenSquare(n):
    arr = [[(n*y)+x+1 for x in range(n)]for y in range(n)]

    for i in range(0, n//4):
        for j in range(0, n//4):
            arr[i][j] = (n*n + 1) - arr[i][j]

    for i in range(0, n//4):
        for j in range(3 * (n//4), n):
            arr[i][j] = (n*n + 1) - arr[i][j]

    for i in range(3 * (n//4), n):
        for j in range(0, n//4):
            arr[i][j] = (n*n + 1) - arr[i][j]

    for i in range(3 * (n//4), n):
        for j in range(3 * (n//4), n):
            arr[i][j] = (n*n + 1) - arr[i][j]

    for i in range(n//4, 3 * (n//4)):
        for j in range(n//4, 3 * (n//4)):
            arr[i][j] = (n*n + 1) - arr[i][j]

    for i in range(n):
        for j in range(n):
            print('%2d ' % (arr[i][j]), end=" ")
        print()


def generateSinglyEvenSquare(n):
    magicsqr = [[0]*n for i in range(n)]
    halfN = n // 2
    k = (n-2)//4
    temp = 0
    swapCol = []
    index = 0
    miniMagic = [[0]*halfN for i in range(halfN)]
    miniMagic = odd(miniMagic)

    for i in range(halfN):
        for j in range(halfN):
            magicsqr[i][j] = miniMagic[i][j]
            magicsqr[i+halfN][j+halfN] = miniMagic[i][j] + halfN*halfN
            magicsqr[i][j+halfN] = miniMagic[i][j] + 2*halfN*halfN
            magicsqr[i+halfN][j] = miniMagic[i][j] + 3*halfN*halfN

    for i in range(1, k+1):
        swapCol.append(i)

    for i in range(n-k+2, n+1):
        swapCol.append(i)

    for i in range(1, halfN+1):
        for j in range(1, len(swapCol)+1):
            temp = magicsqr[i-1][swapCol[j-1]-1]
            magicsqr[i-1][swapCol[j-1]-1] = magicsqr[i+halfN-1][swapCol[j-1]-1]
            magicsqr[i+halfN-1][swapCol[j-1]-1] = temp

    temp = magicsqr[k][0]
    magicsqr[k][0] = magicsqr[k+halfN][0]
    magicsqr[k+halfN][0] = temp

    temp = magicsqr[k+halfN][k]
    magicsqr[k+halfN][k] = magicsqr[k][k]
    magicsqr[k][k] = temp

    for i in range(len(magicsqr)):
        for j in range(len(magicsqr[0])):
            print(magicsqr[i][j], end=' ')
        print()


def odd(magic):
    n = len(magic)
    row = n - 1
    col = n // 2
    magic[row][col] = 1
    for i in range(2, n * n + 1):
        if magic[(row+1) % n][(col+1) % n] == 0:
            row = (row + 1) % n
            col = (col + 1) % n
        else:
            row = (row - 1 + n) % n
        magic[row][col] = i
    return magic


n = int(input("Value Of N? "))
if n == 2:
    sq = [[1, 1], [1, 1]]
    for i in range(len(sq)):
        for j in range(len(sq)):
            print(sq[i][j], end=' ')
        print()
elif n % 2 == 1:
    generateOddSquare(n)
elif n % 4 == 0:
    generateDoublyEvenSquare(n)
else:
    generateSinglyEvenSquare(n)
