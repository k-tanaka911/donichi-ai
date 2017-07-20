import ai

from ai.ai import *

def output(text):
    print("ななこ: " + text)

if __name__ == "__main__":
    output('ななこが、あなたの就職に関するお悩みを、な～んでも聞くよ！')
    output('ななこに言葉を覚えさせたいときは@から初めてね！')

    while True:
        user_input = input("あなた: ")
        if user_input == "": continue
        if user_input == "さようなら": break

        output(Ai.nanako_answer(user_input))

    output("ありがとう☆　またお話しようね♪")
