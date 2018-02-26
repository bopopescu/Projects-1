# age = 26
# user_guess = int(input("your guess :"))
# if user_guess == age:
#     print("恭喜你答对了，中大奖")
# elif user_guess < age:
#     print("try bigger")
# else:
#     print("try smbting")
fraction = int(input("fraction :"))
if fraction > 100:
    print("满分 优秀 ")
elif fraction >= 90:
     print("优加 ")
elif fraction >= 80:
    print("优秀")
elif fraction >= 70:
    print("优良")
elif fraction >= 60:
    print("良")
elif fraction >=0:
    print("成绩不等于零")
else:
    print("差劲 ")