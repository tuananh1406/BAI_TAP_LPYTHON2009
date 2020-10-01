# coding: utf-8
from math import ceil


def theatre_square(n, m, a):
    n_1 = ceil(n/a)
    m_1 = ceil(m/a)
    return n_1 * m_1

if __name__ == '__main__':
    n,m,a = input().split(' ')
    kq = theatre_square(int(n), int(m), int(a))
    print(kq)
