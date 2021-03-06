#! coding: utf-8
'''
Đề bài: Hôm nay là ngày nghỉ, Ben cùng chơi một trò chơi với các bạn của mình.Luật trò chơi rất đơn giản, mỗi người sẽ nhận được một con số nguyên dươnggồm có 5 chữ số. Nếu ai có số nút từ con số này là lớn nhất thì chiến thắng.Hãy giúp Ben tính xem số nút của con số mình nhận được là bao nhiêu.Số nút của một con số là chữ số cuối cùng của tổng các chữ số của con số đó.Ví dụ số 12345 có tổng của các chữ số là 1 + 2 + 3 + 4 + 5 = 15,vậy số nút của nó là chữ số cuối cùng của 15 là con số 5
'''


def tinh_nut(so):
    '''
    Hàm tính số nút của người chơi, input là 1 số nguyên dương bất kỳ.
    Chưa có yêu cầu bắt buộc về đầu vào.
    '''
    so = str(so)
    sum = 0
    for chu_so in so:
        sum += int(chu_so)
    return str(sum)[-1]

if __name__ == '__main__':
    so = input('Nhập số của bạn: ')
    ket_qua = tinh_tong(so)
    print('Số nút của bạn là: %s' %(ket_qua))
