#introuce random
import random

#建立随机单词库
dictionary=("cat","dog","rabbit","bear","sheep")
def hangman(word): #関数を定義
    wrong = 0#エラー数
    HP = ["",
              "_______      ",
              "|      |     ",
              "|      |     ",
              "|      |     ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    data = list(word)#リリースリストWORD
    board = ["_"] * len(word)#ランダムな語長に基づく下線，
    win = False#デフォルトは失敗です
    print("単語当てゲームへようこそ!(動物)")
    while wrong < len(HP) - 1:#回数がヘルス値より小さい場合、実行を継続します
        print("\n")
        msg = "アルファベットを入力してください! "
        char = input(msg)#アルファベットを入力してください!
        if char in data:#判断のメカニズムは、アルファベットが正しければ
            cind = data.index(char)#アルファベットの位置を判断する
            board[cind] = char#アルファベットを置き換える
            data[cind] = '0'#データベースの判定順序を更新する
        else:#エラーカウンタはエラーカウンタが1加算される
            wrong += 1
        print(" ".join(board))#正しくても間違っても単語板を印刷する
        e = wrong + 1
        print("\n".join(HP[0:e]))#小人の失敗位置を記録する
        if "_" not in board:#如結果単語が全て負ければ勝ちとなり、単語が印刷される
            print("勝利!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(HP[0:wrong+1]))#HPが足りなければ失敗する
        print("あなたは失敗しました。正解は{}".format(word))
sblsy = random.choice(dictionary)#単語を無作為に抽出する
hangman(sblsy)