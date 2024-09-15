# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 02:49:04 2024

@author: trankieuvy
"""

id=input("Nhập vào ID của bạn: ")
kytukhonghople="! @#$%^&*()-=+"

idhople = True
for i in id:
    if i in kytukhonghople or i == ' ':
        idhople = False
        break
    
if len(id)<6 and len(id)>24 or not idhople:
    print("ID User của bạn không hợp lệ")
else:
    print("ID User của bạn hợp lệ")
    
password=input("Nhập vào password của bạn: ")

chucaithuong=False
chuso=False
chucaiinhoa=False
kytudacbiet1=False
kytudacbiet="$#@"

for i in password:
    if i.islower():
        chucaithuong = True
    elif i.isupper():
        chucaiinhoa = True
    elif i.isdigit():
        chuso = True
    elif i in kytudacbiet:
        kytudacbiet1 = True
if (chucaithuong and chuso and chucaiinhoa and kytudacbiet1 and 
    6 <= len(password) <= 24):
    print("Password của bạn hợp lệ")
else:
    print("Password của bạn hợp lệ")


        
    
 