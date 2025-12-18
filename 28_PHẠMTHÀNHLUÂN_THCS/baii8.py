a = [1, 2, 3, 4, 5]
n = int(input("Nhập n: "))
n = 0
for _ in a:
    n += 1
n = n % n
while n > 0:
    cuoi = a[n-1]
    i = n - 1
    while i > 0:
        a[i] = a[i-1]
        i -= 1
    a[0] = cuoi
    n -= 1
print("Danh sách sau nhi dịch:", a)