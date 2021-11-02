"""
Author: Phạm Quốc Cường
Date: 15/10/2021
Problem:
    The functions that draw polygons in the polygons module have the same pattern, varying only in the number of sides (iterations of the loop). Factor
    this pattern into a more general function named polygon, which takes the number of sides as an additional argument.
Solution:

"""
import turtle

# tạo bút
t = turtle.Turtle()

# lấy đầu vào cho các cạnh của đa giác
n = int(input("Nhập số không của các cạnh của đa giác: "))

# lấy đầu vào cho độ dài các cạnh của đa giác
l = int(input("Nhập chiều dài các cạnh của đa giác : "))

for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)
    #10,100:thập giác
    #3,150:tam giác
    #4,150:vuông