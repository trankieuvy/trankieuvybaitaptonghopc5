# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:29:13 2024

@author: trankieuvy
"""
chuoi=input("Nhập vào chuỗi: ")
dodai=len(chuoi)
print("Độ dài chuỗi là: ",dodai)

kytudacbiet="!@#$%^&*()-=+./"

demkytudacbiet=0
demchucaithuong=0
demchuso=0
demchucaihoa=0

for i in chuoi:
    if i in kytudacbiet:
        demkytudacbiet+=1
    elif i.islower():
        demchucaithuong+=1
    elif i.isdigit():
        demchuso+=1
    elif i.isupper():
        demchucaihoa+=1
print("Số ký tự đặc biệt là: ",demkytudacbiet)
print("Số ký tự chữ thường là:",demchucaithuong)
print("Số ký tự chữ số là:",demchuso)
print("Số ký tự chữ in hoa là:",demchucaihoa)


        
        