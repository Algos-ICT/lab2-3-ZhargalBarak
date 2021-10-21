def Max_Sub_Arr(A):
    max_sum = float('-inf')
    max_begin, max_end = 0, 0
    cur_sum = 0
    cur_begin = 0
    for cur_end, elem in enumerate(A):
        if cur_sum <= 0:
            cur_begin = cur_end
            cur_sum = elem
        else:
            cur_sum += elem
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_begin = cur_begin
            max_end = cur_end
    return max_sum, max_begin, max_end

file = open('input.txt')
n = int(file.readline())
M = list(map(int, file.readline().split()))
file.close()
res, f, l = Max_Sub_Arr(M)
file = open('output.txt', 'w')
for i in range(f, l+1):
    file.write(str(M[i]) + ' ')
file.write('\n' + str(res) + ' ' + str(f) + ' ' + str(l))
file.close()

