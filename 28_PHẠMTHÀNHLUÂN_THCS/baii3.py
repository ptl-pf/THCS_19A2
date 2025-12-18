chuoi = input("Nhập chuỗi : ")
kt = "" 
khoang_trong = True
for i in chuoi :
    if i != " " :
        kt +=i
        khoang_trong=False
    else :
        if khoang_trong == False :
            kt+=" "
        khoang_trong = True
print(kt)
