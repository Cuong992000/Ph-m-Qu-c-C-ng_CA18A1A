"""
Author: Phạm Quốc Cường
Date: 8/10/2021
Problem:
    Explain the difference between structural equivalence and object identity.
Solution:
Các đối tượng nhận dạng đề cập đến khi chúng ta tạo bí danh để một biến và muốn kiểm tra xem họ có cả hai đề
cập đến cùng một đối tượng hay không. Điều đó có nghĩa là hai biến khác nhau tham chiếu đến cùng một đối
tượng.
Các “là” nhà điều hành có thể được sử dụng để kiểm tra nhận dạng đối tượng. Nó trả về "True" nếu hai biến tham
chiếu đến cùng một đối tượng và nó trả về "False" nếu các biến tham chiếu đến các đối tượng khác nhau.
Hãy xem xét ví dụ sau giải thích về nhận dạng đối tượng.
a = 10
b = a
Bây giờ cả hai biến “a” và “b” đều tham chiếu đến cùng một đối tượng hoặc giá trị 10.
"""