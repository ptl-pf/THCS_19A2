A = [1,2,3,4]
B = [3,4,5,6]
def cac_phep_toan_tap_hop(a,b):
    giao=[x for x in a for y in b if x==y]
    a_khong_b=[x for x in a if all(x!=y for y in b)]
    b_khong_a=[y for y in b if all(y!=x for x in a)]
    return a_khong_b,b_khong_a,giao,a+b_khong_a
print(cac_phep_toan_tap_hop(A,B))
