t = (1,2,3,4,5,6,7,8,9,10)

def tach_chan_le_tu_tuple(t):
    chan, le = [], []
    tong_chan = tong_le = 0
    for num in t:
        if num % 2 == 0:
            chan.append(num)
            tong_chan += num
        else:
            le.append(num)
            tong_le += num
    return tuple(chan), tuple(le), tong_chan, tong_le
chan, le, tong_chan, tong_le = tach_chan_le_tu_tuple(t)
print(chan)        
print(le)          
print(tong_chan)   
print(tong_le)     