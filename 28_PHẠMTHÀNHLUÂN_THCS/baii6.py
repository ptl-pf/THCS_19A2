n = [1,2,3,4,5,6,7,8,9]
tong_chan = 0
tong_le = 0 
for i in n :
    if i %2 == 0 :
        tong_chan+=i
    else :
        tong_le+=i
print(f"Tổng các số chẵn trong danh sách : {tong_chan}")
print(f"Tổng các số lẻ trong danh sách : {tong_le}")