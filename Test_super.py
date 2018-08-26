class FooParent(object):
    def __init__(self):
        self.parent = 'I am the parent.'
        print('Parent')

    def bar(self, message):
        print(message, 'from Parent')


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()  # 意思跟上面差不多，只是这里直接调用的super寻找父辈函数，然后用了super的__init__()
        print('Child')

# 这一点在多重继承时体现得很明显。在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）。
    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child bar function. ')
        print(self.parent)


if __name__ == "__main__":
    a = FooChild()
    a.bar("hi")
