# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:42:16 2024

@author: trankieuvy

"""
import random

luachon = ["kéo", "búa", "bao"]

def chonngaunhien():
    return random.choice(luachon)

def ketqua(nguoi1, nguoi2):
    if nguoi1 == nguoi2:
        return "Hòa"
    elif (nguoi1 == "kéo" and nguoi2 == "bao") or (nguoi1 == "búa" and nguoi2 == "kéo") or (nguoi1 == "bao" and nguoi2 == "búa"):
        return "Người 1 thắng"
    else:
        return "Người 2 thắng"

songuoi = random.randint(8, 20)
print("Số người chơi: ", songuoi)

nguoichoi = [chonngaunhien() for _ in range(songuoi)]
diem = [0] * songuoi

for vong in range(songuoi - 1):
    for i in range(0, songuoi, 2):
        if i + 1 < songuoi:
            nguoi1 = nguoichoi[i]
            nguoi2 = nguoichoi[i + 1]
            print("Người", i + 1, "chọn", nguoi1, "- Người", i + 2, "chọn", nguoi2)
            
            ketquavong = ketqua(nguoi1, nguoi2)
            print("Kết quả:", ketquavong)
            
            if ketquavong == "Người 1 thắng":
                diem[i] += 1
            elif ketquavong == "Người 2 thắng":
                diem[i + 1] += 1

print("\nĐiểm số cuối:")
for i in range(songuoi):
    print("Người", i + 1, ": ", diem[i], "điểm")

