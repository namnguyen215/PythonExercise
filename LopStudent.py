class SinhVien():
    def __init__(self,ten,diemcc,diemkt,diembtl,diemthi):
        self.ten=ten
        self.diemcc=diemcc
        self.diemkt=diemkt
        self.diembtl=diembtl
        self.diemthi=diemthi
    def tinhDiem(self):
        return self.diemcc*0.1+self.diemkt*0.1+self.diembtl*0.2+self.diemthi*0.6
    
    def tinhRank(self):
        diem=self.tinhDiem()
        if(diem>=8.5): return "A Gioi"
        if(diem>=7.0): return "B Kha"
        if(diem>=5.5): return "C Trung binh"
        if(diem>=4.0): return "D Trung binh kem"
        return "F Kem"
    
ten=input()
diemcc=float(input())
diemkt=float(input())
diembtl=float(input())
diemthi=float(input())
tmp=SinhVien(ten,diemcc,diemkt,diembtl,diemthi)
print(tmp.ten+" "+tmp.tinhRank())
        