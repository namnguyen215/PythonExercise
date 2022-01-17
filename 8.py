# MONTHLY SALARY
def cacKhoanKhauTru(LuongCoBan):
    # Các khoản khấu trừ (2) = BHXH + BHYT + BHTN + ĐP + TNCN
    bhxh = LuongCoBan * 8 / 100
    bhyt = LuongCoBan * 1.5/100
    bhtn = LuongCoBan * 1/100
    dp = LuongCoBan * 1/100
    tncn = thu


def run(thuNhapThucTe, LuongCoBan):

    thucLinh = thuNhapThucTe - cacKhoanKhauTru


n = int(input())
if n > 10 or n < 0:
    print("INVALID INPUT")
else:
    for _ in range(n):
        m, n = [float(x) for x in input().split()]
        if m < 1000 or n < 1000:
            print("INVALID INPUT")
        else:
            run(m, n)
