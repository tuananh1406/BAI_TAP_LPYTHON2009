# coding: utf-8


def lay_so_lon_nhat(ds):
    if ds[0] > ds[-1] or len(ds) <= 1:
        return 0
    if ds[-1] > ds[0]:
        return -1

def game_scores(n, ds_the_bai):
    a = []
    b = []
    while True:
        try:
            the_lon_nhat = lay_so_lon_nhat(ds_the_bai)
            a.append(ds_the_bai.pop(the_lon_nhat))
            the_lon_nhat = lay_so_lon_nhat(ds_the_bai)
            b.append(ds_the_bai.pop(the_lon_nhat))
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
