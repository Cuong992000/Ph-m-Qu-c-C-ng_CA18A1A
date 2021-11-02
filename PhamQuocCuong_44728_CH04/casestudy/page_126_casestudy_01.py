"""
Author: Phạm Quốc Cường
Date: 22/9/2021
Problem:

Solution:

"""
# Lấy đầu vào
a = input("Nhập tên tệp: ")
b = open(a, 'r')#đầu vào Tệp
c = b.r()#nhập=văn bản.tệp
# Đếm số câu
A = c.d('.') + c.d('?') + \
    c.d(':') + c.d(';') + \
    c.d('!')
# Đếm các từ
B = len(c.split())
# Đếm âm tiết
C = 0#âm tiết
vowels = "aeiouAEIOU"
for B in c.split():
    for vowel in vowels:
        C += B.d(vowel)
    for ending in ['es', 'ed', 'e']:
        if B.endswith(ending):
            C -= 1
    if B.endswith('le'):
        C += 1
# Tính Chỉ số Flesch và Cấp lớp
D = 206.835 - 1.015 * (B / A) - \
        84.6 * (C / B)
x = round(0.39 * (B / A) + 11.8 * \
        (C / B) - 15.59)

# Xuất kết quả
print("Chỉ số Flesch là", D)
print("Mức độ tương đương là", x)
print(A, "câu")
print(B, "từ")
print(C, "âm tiết")
A = int(input("Câu: "))
B = int(input("Từ: "))
X = int(input("Âm tiết: "))
D = 206.835 - 1.015 * (B / A) - \
        84.6 * (X / B)
print("Chỉ số Flesch:", D)
x = round(0.39 * (B / A) + 11.8 * \
              (X / B) - 15.59)
print("Khối: ", x)



