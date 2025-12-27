with open("san_pham.txt","w",encoding="utf-8") as f :
    f.write("ID,Tên sản phẩm,Gía \n" 
    "1,Laptop, 1200 \n"
    "2,Chuột máy tính,25 \n" 
    "3,Bàn phím, 75")

sua_id = input("Nhập ID : ")
new_gia = input("Nhập giá mới : ")
new_list = []
with open("san_pham.txt","r",encoding="utf-8") as f :
    for new in f:
        id ,ten, gia =new.strip().split(",")
        if id == sua_id:
            gia = new_gia
        new_list.append(f"{id},{ten},{gia}")
with open("san_pham.txt","w",encoding="utf-8") as f :
    for new in new_list:
        f.write(new + "\n")
