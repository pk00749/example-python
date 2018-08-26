# def tag(func):
#     def wrapper(text):
#         value = func(text)
#         return "p" + value + "p"
#     return wrapper
#
# @tag
# def my_upper(text):
#     value = text.upper()
#     return value
#
# if __name__ == '__main__':
#     print(my_upper("hello"))

class A(object):
    def f(self):
        print("f")
def ff():
    print("ff")
a=A()
a.f()
xf=a.f
xf()
a.f=ff
a.f()