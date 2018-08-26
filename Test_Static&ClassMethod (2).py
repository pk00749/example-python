# class A:
#     bar = 1
#     def foo(self):
#         print('foo')
#
#     @staticmethod
#     def static_foo():
#         print('static_foo')
#         print(A.bar)
#
#     @classmethod
#     def class_foo(cls):
#         print('class_foo')
#         # print(cls.bar)
#         # cls().foo()
#         cls().foo()
#         print(cls) # <class '__main__.A'>
#         print(cls()) # <__main__.A object at 0x01C76630>
#         b = cls().foo() # make instance by object
#         return b # return instance
#
#     def test(self):
#         self.foo()
#         print(self.foo())
#
# print(A.bar) # ok, directly quoted
# # A.foo() # false, need instance
# A.static_foo()
# A.class_foo()
# print('-----------')
# b=A.static_foo()
# print('-----------')
#
#
# a = A()
# a.test()



class Date():
    def __init__(self,year=0, month=0,day=0):
        self.year = year
        self.month = month
        self.day = day

    def time(self):
        print("{year}-{month}-{day}".format(year=self.year,month=self.month,day=self.day))

    @classmethod
    def from_string(cls, string):
        year,month,day=map(str,string.split('-'))
        date = cls(year,month,day)
        # return date

date = Date.from_string('2016-11-29')
date.time()
date_old=Date('2016', '11', '29')
date_old.time()
