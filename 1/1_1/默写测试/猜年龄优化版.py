# 要求：
#
# 允许用户最多尝试3次
# 每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，如果回答N或n，就退出程序
# 如何猜对了，就直接退出age_of_oldboy = 48



# age = int(input('Age :'))

'''
Age_gessu = 28
conut = 0
# while  True:
while conut <3:
    age = int(input('Age :'))
    # while conut <= 3:

    if Age_gessu < age :
        print("猜的太大了，往小里试试...")

    elif Age_gessu > age:
         print("猜的太小了，往大里试试...")
    else:
         print('恭喜你猜对了 ....')
    conut += 1
'''
#
# Age_gessu = 28
# conut = 0
# while  conut < 3:
#     age = int(input('Age :'))
#     if Age_gessu < age :
#         print("猜的太大了，往小里试试...")
#     elif Age_gessu > age:
#          print("猜的太小了，往大里试试...")
#     else:
#          print('恭喜你猜对了 ....')
#     conut += 1
#     if  conut == 3:
#         choice = input("你个笨蛋 继续吗(y/n)")
#         if  choice == 'y' or choice == 'y':
#             conut = 0
# *******************************************************
age = 48
num = 0
age1 = 0
while True:
    age1 = int(input("Age: "))
    if age1 == age and num < 3:
        print("答对了")
        break
    else:
        num+=1
        if num >= 3:
            print("是否继续?(y/n)")
            num = 0
            ss = input()
            if(ss == "y"):
                continue
            else:
                break
        else:
            print("继续")
            continue