import csv 
with open("nhan_vien.csv","w",encoding="utf-8") as f :
    writer = csv.writer(f)
    writer.writerow(["ID","Tên","Lương"])
    writer.writerow([1,"Thanh",30000])
    writer.writerow([2,"Hoa",60000])
    writer.writerow([3,"Hong",55555])
    writer.writerow([4,"Kien",36000])
with open("nhan_vien.csv","r",encoding="utf-8") as f :
    reader = csv.DictReader(f)
    for i in reader :
        if int(i["Lương"]) > 50000 :
            print(i)