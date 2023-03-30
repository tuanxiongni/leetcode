import random
ran=random.randint(1,100)
flag=True
while flag:
    guess_num=input('输入你猜的数')
    if ran==guess_num:
        print('猜对了')
        flag=False
    else:
        print("重新输入")
