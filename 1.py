#introuce random
import random

#建立随机单词库
dictionary=("cat","dog","rabbit","bear","sheep")
def hangman(word): #定义函数
    wrong = 0#错误的次数
    HP = ["",
              "_______      ",
              "|            ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    rletters = list(word)#释放列表WORD
    board = ["_"] * len(word)#根据随机到的单词长度展现下划线，
    win = False#默认是失败
    print("欢迎来到猜单词(动物)!")
    while wrong < len(HP) - 1:#如果wrong的次数小于生命值就会继续运行
        print("\n")
        msg = "请输入字母! "
        char = input(msg)#请输入字母
        if char in rletters:#判断机制，如果字母正确
            cind = rletters.index(char)#判断单词位置
            board[cind] = char#替换字母
        else:#错误计数器 如果错误计数器就加1
            wrong += 1
        print(" ".join(board))#不管正确还是错误都打印单词板
        e = wrong + 1
        print("\n".join(HP[0:e]))#记录小人的失败位置
        if "_" not in board:#如果单词全部输对就就获胜，并且打印单词
            print("胜利!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(HP[0:wrong+1]))#如果血量不足则失败
        print("您失败了,正确答案是{}".format(word))
sblsy = random.choice(dictionary)#随机抽取单词
hangman(sblsy)