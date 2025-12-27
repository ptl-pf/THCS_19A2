list = [1,2,3,4,5,6,7,8,9]
with open("so_nguyen.txt" ,"w",encoding="utf-8") as f :
    for so in list :
        f.write(str(so)+ "\n")