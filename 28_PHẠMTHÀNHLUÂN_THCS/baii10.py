ma_tran = [[1,2,3],[4,5,6],[7,8,9]]
def hang_max_sum(m):
    max_hang = 0
    max_sum = 0
    for i in range(len(m)):
        s = 0
        for j in range(len(m[i])):
            s += m[i][j]
        if s > max_sum or i == 0:
            max_sum = s
            max_hang = i
    return max_hang
print(hang_max_sum(ma_tran)) 