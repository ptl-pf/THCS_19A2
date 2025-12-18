dic = {'Anh' : 9 , 'Huy':8,'Thao':9,'Yen':7}
ds = {}
for i in dic :
    diem = dic[i]
    if diem not in ds :
        ds[diem] = [i]
    else : 
        ds[diem].append(i)
print(ds)