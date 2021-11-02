"""
Author: Phạm Quốc Cường
Date: 10/9/2021
Problem:

Solution:

"""

import random
hedges = ("Vui lòng cho tôi biết thêm.",
          "Nhiều bệnh nhân của tôi nói với tôi điều tương tự.",
          "Xin vui lòng tiếp tục.")
qualifiers = ("Tại sao bạn nói như vậy ",
              "Bạn có vẻ nghĩ vậy",
              "Bạn có thể giải thích lý do tại sao ")
replacements = {"I":"you", "me":"you", "my":"your",
                "we":"you", "us":"you", "mine":"yours"}
def reply(sentence):
    "" "Tạo và trả về câu trả lời cho câu." ""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)
def changePerson(sentence):
    "" "Thay thế đại từ ngôi thứ nhất bằng ngôi thứ hai đại từ. "" "
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
        return " ".join(replyWords)
def main():
    "" "Xử lý sự tương tác giữa bệnh nhân và bác sĩ." ""
    print("Chào buổi sáng, tôi hy vọng bạn hôm nay khỏe.")
    print("Tôi có thể làm gì cho bạn?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Chúc một ngày tốt lành!")
            break
            print(reply(sentence))
# The entry point for program execution
if __name__ == "__main__":
    main()
