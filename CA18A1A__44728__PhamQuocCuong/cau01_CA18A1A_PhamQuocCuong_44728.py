"""
Đề thi 02
Date: 30/10/2021
Phạm Quốc Cường

"""
def Cau1():
    def snt(n):
        """ kiểm tra số nguyên tố """
        f = True
        for j in range(2, n):
            if n % j == 0:
                f = False
                break
        return f

    def in_snt(a=5, b=100):
        print("Danh sách số nguyên tố là:")
        """kiểm tra số nguyên tố từ a đến b"""
        for i in range(a, b+1):
            if snt(i):
                print(i, end="  ")
    print()
    # thực thi tìm số nguyên tố
    in_snt(5, 100)

if __name__ == '__main__':
        Cau1()