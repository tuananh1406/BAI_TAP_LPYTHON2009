# coding: utf-8
import re


def remove_zeros(a, b):
    a_no_zero = re.sub('0', '', str(a))
    a_no_zero = int(a_no_zero)
    b_no_zero = re.sub('0', '', str(b))
    b_no_zero = int(b_no_zero)
    tong = a + b
    tong_no_zero = re.sub('0', '', str(tong))
    if int(tong_no_zero) == (a_no_zero + b_no_zero):
        return 'Yes'.upper()
    else:
        return 'No'.upper()

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    kq = remove_zeros(a, b)
    print(kq)
