def nhan_ma_tran(a,b):
    if len(a[0]) != len(b):
        return None
    ket_qua = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                ket_qua[i][j] += a[i][k] * b[k][j]
    return ket_qua

# Ví dụ:
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
print(nhan_ma_tran(A,B))  