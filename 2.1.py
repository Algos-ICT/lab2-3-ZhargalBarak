def Merge_Sort(A, f, l):
    if f < l:
        m = (f + l)//2
        Merge_Sort(A, f, m)
        Merge_Sort(A, m+1, l)
        Merge(A, f, m, l)
        print(f, l, A[f], A[l])

def Merge(A, f, m, l):
    n1 = m - f + 1
    n2 = l - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = A[f + i]
    for j in range(n2):
        R[j] = A[m + j + 1]
    i, j = 0, 0
    for k in range(f, l+1):
        if i < n1 and (j >= n2 or L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

f = open('input.txt')
n = int(f.readline())
M = list(map(int, f.readline().split()))
Merge_Sort(M, 0, n-1)
f.close()
f = open('output.txt', 'w')
for i in range(n):
    f.write(str(M[i]) + ' ')
f.close()