def add(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def sub(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def shtrass(A, B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        m = n//2
        A11 = [[0 for i in range(m)] for j in range(m)]
        A12 = [[0 for i in range(m)] for j in range(m)]
        A21 = [[0 for i in range(m)] for j in range(m)]
        A22 = [[0 for i in range(m)] for j in range(m)]

        B11 = [[0 for i in range(m)] for j in range(m)]
        B12 = [[0 for i in range(m)] for j in range(m)]
        B21 = [[0 for i in range(m)] for j in range(m)]
        B22 = [[0 for i in range(m)] for j in range(m)]

        for i in range(m):
            for j in range(m):
                A11[i][j] = A[i][j]
                A12[i][j] = A[i][j+m]
                A21[i][j] = A[i+m][j]
                A22[i][j] = A[i+m][j+m]

                B11[i][j] = B[i][j]
                B12[i][j] = B[i][j+m]
                B21[i][j] = B[i+m][j]
                B22[i][j] = B[i+m][j+m]

        P1 = shtrass(A11, sub(B12, B22))
        P2 = shtrass(add(A11, A12), B22)
        P3 = shtrass(add(A21, A22), B11)
        P4 = shtrass(A22, sub(B21, B11))
        P5 = shtrass(add(A11, A22), add(B11, B22))
        P6 = shtrass(sub(A12, A22), add(B21, B22))
        P7 = shtrass(sub(A11, A21), add(B11, B12))

        C11 = sub(add(P4, P5), sub(P2, P6))
        C12 = add(P1, P2)
        C21 = add(P3, P4)
        C22 = sub(add(P1, P5), add(P3, P7))

        for i in range(m):
            for j in range(m):
                C[i][j] = C11[i][j]
                C[i][j+m] = C12[i][j]
                C[i+m][j] = C21[i][j]
                C[i+m][j+m] = C22[i][j]
    return C

def Is_Power_Of2(num):
    while num > 1:
        if num % 2 != 0:
            return False
        num //= 2
    return True

f = open('input.txt')
nf = int(f.readline())
if Is_Power_Of2(nf) == False:
    n = nf
    while Is_Power_Of2(n) == False:
        n += 1
    A = [(list(map(int, f.readline().split())) + [0] * (n-nf)) for i in range(nf)]
    B = [(list(map(int, f.readline().split())) + [0] * (n-nf)) for i in range(nf)]
    for i in range(n-nf):
        A.append([0] * n)
        B.append([0] * n)
else:
    A = [list(map(int, f.readline().split())) for i in range(nf)]
    B = [list(map(int, f.readline().split())) for i in range(nf)]
f.close()
C = shtrass(A, B)
f = open('output.txt', 'w')
for i in range(nf):
    for j in range(nf):
        f.write(str(C[i][j]) + ' ')
    f.write('\n')
f.close()