"""
Author: Phạm Quốc Cường
Date: 27/8/2021
Problem:
        Explain what goes on behind the scenes when your computer runs a Python program.
Solution:
        Hậu trường khi thực hiện các chương trình python:
    • Trình thông dịch đọc các câu lệnh và kiểm tra lỗi cú pháp. Nếu tìm thấy bất kỳ lỗi nào thì nó sẽ tạm dừng quá trình và trả về thông báo lỗi.
    • Nếu không tìm thấy lỗi thì trình thông dịch chuyển đổi các câu lệnh python thành ngôn ngữ cấp thấp được gọi là byte –codes.
    • Mã byte này được thực thi bởi một máy ảo python (PVM) và nếu PVM tìm thấy bất kỳ lỗi nào thì nó sẽ tạm dừng việc thực thi và trả về thông báo lỗi.
    • Nếu PVM không tìm thấy lỗi thì nó sẽ đưa ra kết quả cuối cùng.
"""