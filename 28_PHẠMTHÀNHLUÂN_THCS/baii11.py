ma_tran_1 = [[1,2,3],[2,4,5],[3,5,6]]
ma_tran_2 = [[1,2,3],[4,5,6],[7,8,9]]
def doi_xung(m):
    n = len(m)
    for i in range(n):
        for j in range(i+1, n):
            if m[i][j] != m[j][i]:
                return False
    return True
print(doi_xung(ma_tran_1)) 
print(doi_xung(ma_tran_2))