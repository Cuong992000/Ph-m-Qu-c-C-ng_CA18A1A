"""
Author: Phạm Quốc Cường
Date: 27/8/2021
Problem:
        Miranda has forgotten to complete an arithmetic expression before the end of a line of code. How will the Python interpreter react?
Solution:
        Nếu một biểu thức không được xác định hoàn toàn thì trình thông dịch sẽ in ra một thông báo lỗi là “invalid syntax”.
    • Trình thông dịch kiểm tra lỗi cú pháp. Nó sẽ kiểm tra cuối dòng sau biểu thức trước khi tính kết quả và nếu không tìm thấy thì nó sẽ trả về lỗi.
       vd: SyntaxError: invalid syntax
"""