#! coding: utf-8
'''
Đề bài: Hôm nay là ngày nghỉ, Ben cùng chơi một trò chơi với các bạn của mình.Luật trò chơi rất đơn giản, mỗi người sẽ nhận được một con số nguyên dươnggồm có 5 chữ số. Nếu ai có số nút từ con số này là lớn nhất thì chiến thắng.Hãy giúp Ben tính xem số nút của con số mình nhận được là bao nhiêu.Số nút của một con số là chữ số cuối cùng của tổng các chữ số của con số đó.Ví dụ số 12345 có tổng của các chữ số là 1 + 2 + 3 + 4 + 5 = 15,vậy số nút của nó là chữ số cuối cùng của 15 là con số 5
'''


'''
Tính toán bằng các toán tử cơ bản
'''

if __name__ == '__main__':
    so = int(input('Nhập số của bạn: '))
    so_1 = so // (10 ** 4)
    so = so % (10 ** 4)
    so_2 = so // (10 ** 3)
    so = so % (10 ** 3)
    so_3 = so // (10 ** 2)
    so = so % (10 ** 2)
    so_4 = so // 10
    so_5 = so % 10
    tong = (so_1 + so_2 + so_3 + so_4 + so_5)
    print('Số nút của bạn là: %s' %(tong % 10))
