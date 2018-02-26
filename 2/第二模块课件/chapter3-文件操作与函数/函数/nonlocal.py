
# x = 0
# def outer():
#     x = 1
#     def inner():
#         x = 2
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
# outer()
# print("global:", x)

# x = 0
# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x = 2
#         print("inner:", x)
#
#     inner()
#     print("outer:", x)
#
# outer()
# print("global:", x)



x = 0
def outer():
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)