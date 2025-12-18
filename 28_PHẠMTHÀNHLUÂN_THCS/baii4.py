n = int(input("Nhập số phần tử: "))
a = []

i = 0
while i < n:
    x = int(input())
    a.append(x)
    i += 1

max1 = None
max2 = None

for x in a:
    if max1 is None or x > max1:
        if max1 is not None and x != max1:
            max2 = max1
        max1 = x
    elif x != max1 and (max2 is None or x > max2):
        max2 = x

print(f"Giá trị lớn thứ hai: {max2}")
