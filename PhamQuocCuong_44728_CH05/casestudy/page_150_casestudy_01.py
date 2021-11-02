"""
Author: Phạm Quốc Cường
Date: 10/9/2021
Problem:

Solution:

"""
import random
# Từ vựng: các từ trong khác nhau 4 phần của bài phát biểu
articles     = ("A", "THE")
nouns        = ("BOY", "GIRL", "BAT", "BALL")
verbs        = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
    "" "Tạo và trả về một câu." ""
    return nounPhrase() + " " + verbPhrase()
def nounPhrase():
    "" "Tạo và trả về một cụm danh từ." ""
    return random.choice(articles) + " " + random.choice(nouns)
def verbPhrase():
    "" "Tạo và trả về một cụm động từ." ""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()
def prepositionalPhrase():
    "" "Tạo và trả về một cụm giới từ." ""
    return random.choice(prepositions) + " " + nounPhrase()
def main():
    "" "Cho phép người dùng nhập số câu cần tạo." ""
number = int(input("Nhập số câu:"))
for count in range(number):
    print(sentence())
# Điểm vào để thực hiện chương trình
if __name__ == "__main__":
    main()
