# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:14:25 2024

@author: trankieuvy

"""

from random import randint
may= randint(1, 3)
nguoi=int(input("Bạn vui lòng chọn: 1. Kéo, 2. Búa, 3. Bao: "))

if may==1:
    print("Máy chọn Kéo")
if may==2:
    print("Máy chọn Búa")
if may==3:
    print("Máy chọn Bao ")
    
if may==nguoi:
    print("Hòa")
if may==1 and nguoi==2:
    print("Thắng")
if may==1 and nguoi==3:
    print("Thua")
if may==2 and nguoi==1:
    print("Thua")
if may==2 and nguoi==3:
    print("Thắng")
if may==3 and nguoi==1:
    print("Thắng")
if may==3 and nguoi==2:
    print("thắng")
    
    