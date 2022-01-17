# TUYEN NHAN VIEN
class ThiSinh:
    def __init__(self, ten: str, lyThuyet: str, thucHanh: str):
        self.ten = ten
        self.lyThuyet = lyThuyet
        self.thucHanh = thucHanh
        self.trungBinh = self.getTrungBinh()

    def getLyThuyet(self):
        if '.' in self.lyThuyet:
            return float(self.lyThuyet)
        elif int(self.lyThuyet) > 10:
            return float(self.lyThuyet)/10
        return float(self.lyThuyet)

    def getThucHanh(self):
        if '.' in self.thucHanh:
            return float(self.thucHanh)
        elif int(self.thucHanh) > 10:
            return float(self.thucHanh)/10
        return float(self.thucHanh)

    def getTrungBinh(self):
        return float((self.getLyThuyet() + self.getThucHanh())/2)

    def getTrangThai(self):
        if self.trungBinh < 5:
            return "TRUOT"
        elif self.trungBinh >= 5 and self.trungBinh < 8:
            return "CAN NHAC"
        elif self.trungBinh >= 8 and self.trungBinh < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

    def __str__(self):
        return f"{self.ten} {self.trungBinh:.2f} {self.getTrangThai()}"


thiSinh_list = []
for _ in range(int(input())):
    tmp = ThiSinh(input(), input(), input())
    thiSinh_list.append(tmp)

thiSinh_list = sorted(thiSinh_list, key=lambda x: (-x.trungBinh, x.ten))
for thiSinh in thiSinh_list:
    print(thiSinh)

''' 
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''
