# count = 0
# while count <= 100:
#     print('loop',count)
#     count += 2

# count = 0
# while count <= 100:
#     if count %2 == 0:
#         print('loop',count)
#     count += 1
#第50次不打印 第60-第80答应对应 的平方
# count = 0
# while count <= 100:
#     if count  == 50:
#         pass   #就是过 也是行符
#     elif count >= 60 and count <= 80:
#         print(count * count)
#     else:
#         print('loop', count)
# #        print('loop',count)
#     count += 1


count = 0
while count <= 5:
    print('loop',count)
    if count == 3:
        break
    count += 1
else:
    print('loop is done,')
print('out of loop')

