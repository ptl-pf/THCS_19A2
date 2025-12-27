with open("vanban.txt", "w",encoding="utf-8") as f :
    f.write("Python là một ngôn ngữ lập trình mạnh mẽ, dễ học và có nhiều ứng dụng. " 
    "Nó được sử dụng rộng rãi trong phát triển web, khoa học dữ liệu, trí tuệ nhân tạo và tự động hóa. "
    "Cộng đồng Python rất lớn và hỗ trợ tuyệt vời, với nhiều thư viện phong phú để giải quyết mọi vấn đề.")

with open("vanban.txt", "r",encoding="utf-8") as f :
    noi_dung = f.read()
ds = noi_dung.split()
tsxh = {}
for tu in ds :
    if tu in tsxh :
        tsxh[tu] +=1
    else :
        tsxh[tu] =1
print("Danh sách và số lần xuất hiện của các từ là :")
for tu , xuat_hien in tsxh.items() :
    print(f"{tu} : {xuat_hien} lần ")