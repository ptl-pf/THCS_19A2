I3 = [[1,0,0],[0,1,0],[0,0,1]]
khong_phai_I = [[1,0,0],[0,2,0],[0,0,1]]
def kiem_tra_ma_tran_don_vi(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if (i == j and m[i][j] != 1) or (i != j and m[i][j] != 0):
                return False
    return True
print(kiem_tra_ma_tran_don_vi(I3))    
print(kiem_tra_ma_tran_don_vi(khong_phai_I)) 