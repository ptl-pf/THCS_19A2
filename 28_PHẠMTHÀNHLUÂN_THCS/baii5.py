a = [1,2,3,1,2,4,5]
b = []
for i in a :
    trung_lap = False
    for x in b :
        if i == x :
            trung_lap = True
    if trung_lap == False :
        b.append(i)
print(f"Danh sách khi loại bỏ các phần tử trùng lặp :{b}")
            

