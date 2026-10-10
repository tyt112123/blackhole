import random
def guess_number():
    print("猜数字小游戏")
    numbers = random.randint(1, 100)
    while True:
        try:
            s = int(input("请输入一个数字："))#try:+except语句用于捕获异常，防止程序崩溃
        except ValueError:
            print("请输入有效数字")
            continue
        if s > numbers:
            print("猜大了")
        elif s < numbers:
            print("猜小了")
        else:
            print("恭喜猜对了")
            break
def add(a,b):
    return a+b
guess_number()
print(add(1,8))
