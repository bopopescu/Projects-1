#!/usr/bin/env python3
#encoding=utf-8
# kevim 
# lau.liu@9street.org

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a+b

        n = n + 1
    return  'done'

# print(fib(10))
# f = fib(10)

g = fib(6)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break

# print('====start loop====')
# for i in  f:
#     print(i)
# #########################
