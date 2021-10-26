def equal(A, B):
    if len(A) > len(B):
        B = [0] * (len(A) - len(B)) + B
    elif len(A) < len(B):
        A = [0] * (len(B) - len(A)) + A
    return A, B

def add(A, B):
    A, B = equal(A, B)
    C = []
    for i in range(len(A)):
        C.append(A[i] + B[i])
    return C

def sub(A, B):
    A, B = equal(A, B)
    C = []
    for i in range(len(A)):
        C.append(A[i] - B[i])
    return C

def karatsuba(A, B):
    A, B = equal(A, B)
    C = []
    if len(A) == 1:
        C.append(A[0] * B[0])
    else:
        n = len(A)
        C = [0 for i in range(2*n - 1)]
        mid = n // 2

        A1 = [0 for i in range(mid)]
        A2 = [0 for i in range(n-mid)]

        B1 = [0 for i in range(mid)]
        B2 = [0 for i in range(n-mid)]

        for i in range(mid):
            A1[i] = A[i]
            B1[i] = B[i]
        for i in range(mid, n):
            A2[i-mid] = A[i]
            B2[i-mid] = B[i]

        C1 = karatsuba(A1, B1)
        C3 = karatsuba(A2, B2)
        C2 = sub(karatsuba(add(A1, A2), add(B1, B2)), add(C1, C3))
        while C2[0] == 0:
            C2.pop(0)

        for i in range(len(C1)):
            C[i] += C1[i]
        for i in range(len(C2)):
            C[i+n//2] += C2[i]
        for i in range(len(C3)):
            C[i+len(C)-len(C3)] += C3[i]
    return C

f = open('input.txt')
n = int(f.readline())
A = list(map(int, f.readline().split()))
B = list(map(int, f.readline().split()))
f.close()
C = karatsuba(A, B)
f = open('output.txt', 'w')
for i in range(2*n-1):
    f.write(str(C[i]) + ' ')
f.close()

