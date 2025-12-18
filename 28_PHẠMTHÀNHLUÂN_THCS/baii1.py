chuoi = input("Nhập chuỗi : ")
ky_tu_chu_cai = 0
ky_tu_chu_so = 0
ky_tu_dac_biet = 0 
for i in chuoi :
    if "a" <= i <= "z" or "A" <= i <= "Z" :
        ky_tu_chu_cai +=1 
    elif "0 "<= i <= "9":
        ky_tu_chu_so+=1
    else :
        ky_tu_dac_biet+=1
print(f"Kí tự chữ cái : {ky_tu_chu_cai}")
print(f"Kí tự chữ số : {ky_tu_chu_so}")
print(f"Kí tự đặc biệt : {ky_tu_dac_biet}")