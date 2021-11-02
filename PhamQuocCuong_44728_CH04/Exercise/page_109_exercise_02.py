"""
Author: Phạm Quốc Cường
Date: 22/9/2021
Problem:
        Consult the Table of ASCII values in Chapter 2 and suggest how you would modify the encryption and decryption scripts in this section to
        work with strings containing all of the printable characters.
Solution:
    Để sửa đổi các tập lệnh mã hóa và giải mã, hãy thay đổi ký tự 'a' trong mã thành ký tự "dấu cách",điều này là như vậy bởi vì phạm vi ký tự in được
    bắt đầu bằng khoảng trắng hình thức 32 và ký tự cuối cùng là ký tự 'Z'
"""
data = "hello uda!"
data[1]
