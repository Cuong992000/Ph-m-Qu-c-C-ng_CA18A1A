"""
Author: Phạm Quốc Cường
Date: 27/8/2021
Problem:
        Suppose your script attempts to print the value of a variable that has not yet been assigned a value.
        How does the Python interpreter react?
Solution:
        Nếu bất kỳ biến nào không được gán bất kỳ giá trị nào thì việc cố gắng in biến đó sẽ dẫn đến thông báo lỗi là
        “variable_name not defined”.
        Trình thông dịch kiểm tra lỗi cú pháp. Nó sẽ kiểm tra giá trị của biến trước khi in ra và nếu không tìm thấy thì nó sẽ trả về lỗi.
        vd:
        Traceback (most recent call last):
        File "<pyshell#l>", line 1, in <module>
        NameError: name 'lenth' is not defined
"""