# g=1
# def fund():
#     g=2
#     return g
# print(fund(),g)


def outer():
    e = 1
    def inner():
        nonlocal e
        e = 2
        print('e in inner:{}'.format(id(e)))
        return e
    print('e in outer:{}'.format(id(e)))
    print(e,inner())
    return inner

outer()
