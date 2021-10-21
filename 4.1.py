def Binary_Search(A, f, l, targ):
    if l < f:
        return -1
    mid = f + (l - f)//2
    if targ == A[mid]:
        return mid
    elif targ < A[mid]:
        return Binary_Search(A, f, mid-1, targ)
    else:
        return Binary_Search(A, mid+1, l, targ)

f = open('input.txt')
n = int(f.readline())
A = list(map(int, f.readline().split()))
k = int(f.readline())
B = list(map(int, f.readline().split()))
f.close()
f = open('output.txt', 'w')
for i in range(len(B)):
    f.write(str(Binary_Search(A, 0, len(A)-1, B[i])) + ' ')
f.close()

