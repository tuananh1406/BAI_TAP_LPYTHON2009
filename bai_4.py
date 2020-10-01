# coding: utf-8


def game_scores(n, ds_the_bai):
    ds_the_bai.sort()
    a = []
    b = []
    while True:
        try:
            a.append(ds_the_bai.pop())
            b.append(ds_the_bai.pop())
        except:
            break
    kq_a = sum(a)
    kq_b = sum(b)
    return kq_a, kq_b

if __name__ == '__main__':
    n = int(input())
    ds = input().split(' ')
    ds = [ int(c) for c in ds ]
    a, b = game_scores(n, ds)
    print(a, b)
