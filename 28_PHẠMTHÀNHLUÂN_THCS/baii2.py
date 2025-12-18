chuoi = input("Nhập chuỗi : ")
n = int(input("Nhập n  : "))
do_dai = ""
for i in chuoi + " ":
    if i !=  " " :
        do_dai +=i 
    else :
        if len(do_dai) > n:
            print(do_dai)
        do_dai= ""
