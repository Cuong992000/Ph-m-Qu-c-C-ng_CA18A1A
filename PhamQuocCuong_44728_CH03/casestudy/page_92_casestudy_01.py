"""
Author: Phạm Quốc Cường
Date: 8/9/2021
Problem:

Solution:

"""
""" 
Tính căn bậc hai của một số. 
1. Đầu vào 
    Một số. 
2. Kết quả đầu ra là:
    Ước lượng của chương trình về căn bậc hai bằng cách sử dụng phương pháp xấp xỉ liên tiếp của Newton,
    và ước tính riêng của Python bằng cách sử dụng math.sqrt.
"""
import math
# Nhận số đầu vào từ người dùng
x = float(input("Nhập một số dương: "))
# Khởi tạo dung sai và ước lượng
y = 0.000001
z = 1.0#ước tính
# Thực hiện các phép tính gần đúng liên tiếp
while True:
    z = (z + x / z) / 2#ước tính
    X = abs(x - z ** 2)#hiệu số
    if X <= y:
        break
# In ra kết quả
print("Ước tính của chương trình:", z)
print("Ước tính của Python:     ", math.sqrt(x))
