# coding: utf-8
from math import sqrt


def tim_nghiem(n, so):
    if (n - so) < 0:
        return None
    nghiem = sqrt((n - so))
    nghiem_2 = int(nghiem)
    if nghiem == float(nghiem_2):
        return nghiem
    else:
        return None

def phuong_trinh(a, b, n, m):
    pt_1 = a**2 + b
    pt_2 = b**2 + a
    if pt_1 == n and pt_2 == m:
        return True
    return False

if __name__ == '__main__':
    n, m = input().split(' ')
    n = int(n)
    m = int(m)
    mang_n = []
    for so_a in range(n):
        if tim_nghiem(n, so_a):
            b = tim_nghiem(n, so_a)
            if tim_nghiem(m, b) is not None:
                a = tim_nghiem(m, b)
                if int(a) == int(so_a):
                    mang_n.append([so_a, b])
    ket_qua = mang_n.copy()
    for a, b in mang_n:
        if phuong_trinh(b, a, m, n):
            if a != b:
                ket_qua.append([b, a])
    print(len(ket_qua))
