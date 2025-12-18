def la_so_nguyen_to(x) :
    if x < 2 : 
        return False
    for i in range(2,x) : 
        if x % i == 0 : 
            return False
    else : 
        return True
x = int(input("Nhập x : "))
lsnt = la_so_nguyen_to(x)
print(lsnt)

print("Các số nguyên tố từ 100 đến 500:")
for y in range(100,501) :
    if la_so_nguyen_to(y) : 
        print(y)

