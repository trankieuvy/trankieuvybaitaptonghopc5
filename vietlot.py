# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 02:44:29 2024

@author: Admin
"""

import random

sove = int(input("Nhập số vé bạn muốn mua: "))
tongtienthang = 0
giave = 10000

sotrungthuong = random.sample(range(1, 46), 6)
print("Dãy số trúng thưởng: ",sotrungthuong)

for i in range(sove):
    ve = random.sample(range(1, 46), 6)
    sotrung = len(set(ve) & set(sotrungthuong))  

# Tính số tiền thưởng
    if sotrung == 6:
        tongtienthang += 10000000000
    elif sotrung == 5:
        tongtienthang += 10000000
    elif sotrung == 4:
        tongtienthang += 300000
    elif sotrung == 3:
        tongtienthang += 30000

    print(f"Vé {i + 1}: {ve} - Trùng {sotrung} số, Thưởng: {tongtienthang:,} vnđ")


tongchiphi = sove * giave
print(f"Tổng tiền trúng: {tongtienthang:,} vnđ")
print(f"Tổng chi phí: {tongchiphi:,} vnđ")
print(f"Lợi nhuận: {tongtienthang - tongchiphi:,} vnđ")
