with open("nguon.txt","w",encoding="utf-8") as f :
    f.write("file nguồn")
with open("nguon.txt","rb") as f_nguon :
    with open("dich.txt","wb" ) as f_dich :
        while True :
            data = f_nguon.read(1024)
            if not data :
                break
            f_dich.write(data)