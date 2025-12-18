dic = {'x': 8, 'y':2,'z':207}
max_key = None
max_val = None
for i in dic :
    if max_val is None or dic[i] > max_val :
        max_val = dic[i]
        max_key = i 
print(max_key)
