#introuce random
import random
def putin():
     print("请输入你想输入的单词!")
     w=input("input:")
     return w
def judgeword(w):
     if w.islower():
          print("全是小写字母，符合")
     else:
          print("不符合，请重新请输入单词")
          aa=putin()
def countword(w):
     res={}
     for i in w:
          res[i]=w.count(i)
          c=len(res)
     print("输入的字符串中共有%d个不同的字母" %c)
aa=putin()
judgeword(aa)
countword(aa)
