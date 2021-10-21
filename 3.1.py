def Merge_Sort(A, f, l):
    if f < l:
        m = (f + l)//2
        res = 0
        res += Merge_Sort(A, f, m)
        res += Merge_Sort(A, m+1, l)
        res += Merge(A, f, m, l)
        return res
    return 0

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
    count = 0
    inver = 0
    for k in range(f, l+1):
        if i < n1 and (j >= n2 or L[i] <= R[j]):
            A[k] = L[i]
            i += 1
            inver += count
        else:
            A[k] = R[j]
            j += 1
            count += 1
    return inver

f = open('input.txt')
M = list(map(int, f.readline().split()))
f.close()
f = open('output.txt', 'w')
f.write(str(Merge_Sort(M, 0, len(M)-1)))
f.close()
