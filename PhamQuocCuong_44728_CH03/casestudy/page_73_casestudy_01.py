"""
Author: Phạm Quốc Cường
Date: 8/9/2021
Problem:

Solution:

"""
""" 
Tính toán báo cáo đầu tư.
1. Các đầu vào    
    Số tiền đầu tư bắt đầu    
    Số năm   
    Lãi suất 
2. Báo cáo được hiển thị dưới dạng bảng với tiêu đề.
3. Tính toán và kết quả đầu ra:   
     Cho mỗi năm   
     Tính toán tiền lãi và thêm nó vào khoản đầu tư       
     In một hàng kết quả được định dạng cho năm đó
4. Khoản đầu tư cuối kỳ và tiền lãi kiếm được cũng được hiển thị.
"""
# Đầu vào
a = float(input("Nhập số tiền đầu tư: "))#tiền đầu tư
b = int(input("Nhập số năm: "))#năm
c = int(input("Nhập tỷ lệ dưới dạng %: "))#tỷ lệ
# Chuyển đổi tỷ lệ thành số thập phân
c = c / 100 #tỷ lệ %
# Khởi tạo bộ tích lũy cho lãi suất
T = 0.0 #tổng số tiền lãi
# Hiển thị tiêu đề cho bảng
print("%4s%18s%10s%16s" % \
      ("Năm",  "Cân bằng",     "Lãi",  "Số dư cuối kỳ"))
# Tính toán và hiển thị kết quả cho mỗi năm
for year in range(1, b + 1):
    A = a * c #Tính lãi
    B = a + A #số dư cuối kỳ
    print("%4d%18.2f%10.2f%16.2f" % \
        (b, a, A, B))
    a = B
    T += A
