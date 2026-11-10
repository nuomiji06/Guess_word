#写命令行版“猜单词游戏”
import random
list1 = ['apple', 'banana', 'orange', 'grape', 'peach']
a = random.choice(list1)
n = len(a)
b = n
print("欢迎来到猜单词游戏！")
print("_" * n)
i = 1
while n > 0:
    s = str(input("请输入你猜的单词的第%d个字母:" % i))
    if s == a[i - 1]:
        print("猜对了！")
        for j in range(i):
            print("%s" % a[j],end="")
        print("_"*(b-1))
        i = i + 1
        b = b - 1
    else:
        if i != 1:
            for j in range(i-1):
                print("猜错了！\n%s" % a[j],end="")
            print("_" * b )
        else:
            print("猜错了！")
            print("_"*b)
        n -= 1
        s = str("你还有%d次机会" % n)
    if i == len(a) + 1:
        print("恭喜你，猜对了！")
        break

print("游戏结束，正确答案是：%s" % a)