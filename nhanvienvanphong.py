# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 16:26:50 2024

@author: trankieuvy

"""
class NVVanPhong:
    def __init__(self, manhanvien, hoten, luongcoban, songay):
        self.manhanvien = manhanvien
        self.hoten = hoten
        self.luongcoban = luongcoban
        self.songay = songay
        self.luongthang = self.tinhluong()

    def tinhluong(self):
        return self.luongcoban * self.songay

    def __str__(self):
        return "NV Văn Phòng: " + self.manhanvien + " - " + self.hoten + " - Lương cơ bản: " + str(self.luongcoban) + " - Số ngày làm: " + str(self.songay) + " - Lương tháng: " + str(self.luongthang)

class NVBanHang:
    def __init__(self, manhanvien, hoten, luongcoban, sosanpham):
        self.manhanvien = manhanvien
        self.hoten = hoten
        self.luongcoban = luongcoban
        self.sosanpham = sosanpham
        self.luongthang = self.tinhluong()

    def tinhluong(self):
        return self.luongcoban + (self.sosanpham * 50000)

    def __str__(self):
        return "NV Bán Hàng: " + self.manhanvien + " - " + self.hoten + " - Lương cơ bản: " + str(self.luongcoban) + " - Số sản phẩm: " + str(self.sosanpham) + " - Lương tháng: " + str(self.luongthang)

danh_sach_nhan_vien = [
    NVVanPhong("VP001", "Nguyễn Văn A", 500000, 22),
    NVVanPhong("VP002", "Trần Thị B", 550000, 20),
    NVVanPhong("VP003", "Lê Văn C", 600000, 25),
    NVVanPhong("VP004", "Phạm Văn D", 520000, 23),
    NVVanPhong("VP005", "Đỗ Thị E", 580000, 21),
    NVBanHang("BH001", "Nguyễn Văn F", 400000, 50),
    NVBanHang("BH002", "Trần Thị G", 450000, 60),
    NVBanHang("BH003", "Lê Văn H", 420000, 45),
    NVBanHang("BH004", "Phạm Văn I", 460000, 70),
    NVBanHang("BH005", "Đỗ Thị K", 430000, 55),
]

for nhan_vien in danh_sach_nhan_vien:
    print(nhan_vien)

