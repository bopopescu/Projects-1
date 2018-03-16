#!/usr/bin/python
#_*_ coding:utf-8 _*_
KEVIM = 'Kevim Liu'
# lau.liu@9street.org
def range2(n):
    conut = 0
    while  conut < n:
        print('conut',conut)
        conut += 1
        yield   conut #return   区别是
    print('------')
    return  3333
9
print(range2(10))
range2(10)
new_range = range2(4)
r1 = next(new_range)
print(r1)
r2 = next(new_range)
print(r2)
next(new_range)

new_range.__next__()


#  yield  vs  return
#  return 返回 并终止function
#  yield  返回 数据 并冻结当前的执行过程
#  next() 唤醒冻结的执行过程  继续执行 直到遇到下一个yield

# 生成器的创方式
#       1 列表 生成式 （）
#       2 函数

# yield    vs return
#  return  返回 并终止function
# yield 返回 数据 并冻结当前的执行过程
#next 唤醒冻结函数执行过程 继续执行 知道遇到下一个yield
#
# 函数有了yield 之后
#
# 1、函数名加（）就变得到了一个生成器
# 2、return 再生成器里，代表 生成器的中止，直接  报错
# next
#    唤醒，生成器并 执行
#send ("stop")
    #1、唤醒并继续执行
    #2、 发送一个信息到生成 器内部