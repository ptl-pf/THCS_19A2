
def tong_cheo_phu(m):
    n = len(m)
    tong = 0
    for i in range(n):
        tong += m[i][n-1-i]
    return tong
ma_tran = [[1,2,3],[4,5,6],[7,8,9]]
print(tong_cheo_phu(ma_tran))
