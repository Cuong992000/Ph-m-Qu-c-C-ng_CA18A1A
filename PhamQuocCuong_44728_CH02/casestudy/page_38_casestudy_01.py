"""
Author: Phạm Quốc Cường
Date: 1/9/2021
Problem:

Solution:
    Tính thuế thu nhập cá nhân :
    1. các hằng số quan trọng
        thuế suất
        khấu trừ tiêu chuẩn
        khấu trừ thêm
    2. Nhập đầu vào
        tổng thu nhập
        số người phụ thộc
    3. công thức tính toán
        thu nhập chịu thuế= tổng thu nhập - khấu trừ tiêu chuẩn - khấu trừ thêm * số người phụ thuộc
        thuế thu nhập cá nhân= Thu nhập tính thuế * Thuế suất.
"""
x=0.20#thuế suất
y=10000#khấu trừ tiêu chuẩn
z=3000#khâu trừ thêm
a=float(input("Nhập tổng thu nhập: $"))
b=int(input("nhập số người phụ thuộc: "))
A=a-y-z*b#thu nhập tính thuế
B=A * x#Thuế thu nhập
print("Thuế TNCN phải nộp là: $",B)

